from datetime import datetime

from celery.result import AsyncResult

from app.logger import logger
from app.reservation.async_redis import RedisClient
from app.reservation.dao import ReservationDAO
from app.reservation.shemas import ReservationCreate, ReservationResponse
from app.tasks.tasks import delete_reservation


class ReservationService:
    """Сервисный слой бронирования книг."""

    @classmethod
    async def create_reservation(cls, reservation: ReservationCreate):
        """Бронирование книги."""
        try:
            new_reservation = await ReservationDAO.reserve_book(reservation)

            logger.info(f"Бронь номер {new_reservation.id} создана")
            #  Период. задача удаления брони в фоновом режиме
            diff_datetime = reservation.end_date - reservation.start_date
            eta_time = datetime.now() + diff_datetime
            result = delete_reservation.apply_async(
                args=[new_reservation.id],
                eta=eta_time,
            )
            logger.info(
                f"Отмена брони номер {new_reservation.id} назначена на "
                f"{eta_time.strftime('%Y-%m-%d %H:%M:%S')}"
            )

            # Добавляем в redis в качестве ключа - ID бронирования,
            # в качестве значения - ID запущенной задачи
            await RedisClient.set(new_reservation.id, result.id)

            return new_reservation
        except Exception as ex:
            logger.error(
                f'Ошибка в бронировании книги: {ex}', exc_info=True,
            )
            raise

    @classmethod
    async def return_book(cls, reservation_id: int) -> ReservationResponse:
        """Отмена брони."""
        reservation = await ReservationDAO.return_book(reservation_id)

        try:
            logger.info("Отмена выполнения фоновой задачи...")
            task_id = await RedisClient.pop(reservation_id)

            assert task_id is not None
            async_res = AsyncResult(str(task_id))
            async_res.revoke(terminate=async_res.ready())

            logger.info(f"Задача номер {task_id.decode('utf-8')} отменена")
            return reservation
        except Exception as ex:
            logger.error(
                f'Ошибка в отмене задачи номер {task_id}: {ex}',
                exc_info=True,
            )
            raise

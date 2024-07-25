from datetime import datetime

from celery.result import AsyncResult

from app.reservation.async_redis import RedisClient
from app.reservation.dao import ReservationDAO
from app.reservation.shemas import ReservationCreate, ReservationResponse
from app.tasks.tasks import delete_reservation


class ReservationService:
    """Сервисный слой бронирования книг."""

    @classmethod
    async def create_reservation(cls, reservation: ReservationCreate):
        """Бронирование книги."""
        new_reservation = await ReservationDAO.reserve_book(reservation)

        #  Удаление брони в фоновом режиме
        diff_datetime = reservation.end_date - reservation.start_date
        result = delete_reservation.apply_async(
            args=[new_reservation.id],
            eta=datetime.now() + diff_datetime,
        )

        # Добавляем в redis в качестве ключа - ID бронирования,
        # в качестве значения - ID запущенной задачи

        await RedisClient.set(new_reservation.id, result.id)
        print("Result ID: ", result.id, type(result.id))

        return new_reservation

    @classmethod
    async def return_book(cls, reservation_id: int) -> ReservationResponse:
        """Отмена брони."""
        reservation = await ReservationDAO.return_book(reservation_id)

        # отменяем выполнение фоновой задачи
        task_id = await RedisClient.pop(reservation_id)

        assert task_id is not None
        async_res = AsyncResult(str(task_id))
        async_res.revoke(terminate=async_res.ready())

        return reservation

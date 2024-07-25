import asyncio

from app.logger import logger
from app.reservation.dao import ReservationDAO
from app.tasks.celery import celery


@celery.task
def delete_reservation(reservation_id: int):
    """Удаление брони для книги."""
    try:
        logger.info("Снятие с книги брони...")
        loop = asyncio.get_event_loop()
        reservation = loop.run_until_complete(
            ReservationDAO.delete_reservation(reservation_id)
        )
        if reservation:
            logger.info(f"Бронь номер {reservation.id} удалена")
            return reservation.id
        else:
            logger.warning(f"Бронь с ID={reservation_id} не нашлась в БД")
    except Exception as ex:
        logger.error(f'Ошибка в удалении брони: {ex}', exc_info=True)
        raise

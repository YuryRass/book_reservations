import asyncio

from app.reservation.dao import ReservationDAO
from app.tasks.celery import celery


@celery.task
def delete_reservation(reservation_id: int):
    """Удаление брони для книги."""
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(
        ReservationDAO.delete(id=reservation_id)
    )

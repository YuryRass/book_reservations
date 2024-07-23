from datetime import datetime

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
        delete_reservation.apply_async(
            args=[new_reservation.id],
            eta=datetime.now() + diff_datetime,
        )

        return new_reservation

    @classmethod
    async def return_book(cls, reservation_id: int) -> ReservationResponse:
        """Отмена брони."""
        return await ReservationDAO.return_book(reservation_id)

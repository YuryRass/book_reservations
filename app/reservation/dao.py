from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session

from app.dao.base import BaseDAO
from app.exceptions import ExistingReservationException, ReservationNotFoundException
from app.reservation.model import Reservation
from app.reservation.shemas import ReservationCreate, ReservationResponse


class ReservationDAO(BaseDAO):
    """CRUD операции для бронирования книг."""

    model = Reservation

    @classmethod
    async def reserve_book(
        cls, reservation: ReservationCreate
    ) -> ReservationResponse:
        """Бронирование книги пользователем на незанятые даты."""
        query = Reservation.__table__.select().where(
            Reservation.book_id == reservation.book_id,
            (Reservation.start_date <= reservation.end_date) &
            (Reservation.end_date >= reservation.start_date)
        )

        session: AsyncSession
        async with async_session() as session:
            res = await session.execute(query)
            existing_reservation = res.scalars().first()

        if existing_reservation is not None:
            raise ExistingReservationException

        return await super().add(**reservation.model_dump())

    @classmethod
    async def return_book(cls, reservation_id: int) -> ReservationResponse:
        """Возврат книги (отмена брони)."""
        reservation = await super().get_by_id(reservation_id)

        if not reservation:
            raise ReservationNotFoundException

        return await ReservationDAO.delete(id=reservation.id)

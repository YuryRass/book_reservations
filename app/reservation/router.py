from fastapi import APIRouter

from app.reservation.dao import ReservationDAO
from app.reservation.shemas import ReservationCreate, ReservationResponse


router: APIRouter = APIRouter(tags=['Reservations'])


@router.post("/reservations/", response_model=ReservationResponse)
async def create_reservation(reservation: ReservationCreate):
    """Бронирование книги."""
    return await ReservationDAO.reserve_book(reservation)


@router.delete("/return/{reservation_id}", response_model=ReservationResponse)
async def return_book(reservation_id: int) -> ReservationResponse:
    """Отмена брони."""
    return await ReservationDAO.return_book(reservation_id)

from datetime import datetime
from fastapi import APIRouter

from app.reservation.dao import ReservationDAO
from app.reservation.shemas import ReservationCreate, ReservationResponse
from app.tasks.tasks import delete_reservation


router: APIRouter = APIRouter(tags=['Reservations'])


@router.post("/reservations/", response_model=ReservationResponse)
async def create_reservation(reservation: ReservationCreate):
    """Бронирование книги."""
    new_reservation = await ReservationDAO.reserve_book(reservation)

    #  Удаление брони в фоновом режиме
    diff_datetime = reservation.end_date - reservation.start_date
    delete_reservation.apply_async(
        args=[new_reservation.id],
        eta=datetime.now() + diff_datetime,
    )

    return new_reservation


@router.delete("/return/{reservation_id}", response_model=ReservationResponse)
async def return_book(reservation_id: int) -> ReservationResponse:
    """Отмена брони."""
    return await ReservationDAO.return_book(reservation_id)

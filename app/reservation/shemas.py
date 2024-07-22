from datetime import datetime, timedelta

from pydantic import Field

from app.base.shema import MainModel


class ReservationBase(MainModel):
    """Основная схема для бронирования книг."""

    id: int | None = Field(
        None,
        description="Уникальный идентификатор брони",
        example=3,
    )
    start_date: datetime = Field(
        ...,
        description="Дата и время бронирования книги",
        example=datetime.now(),
    )
    end_date: datetime = Field(
        ...,
        description="Дата и время окончания бронирования книги",
        example=datetime.now() + timedelta(days=5),
    )

    user_id: int = Field(
        ...,
        description="ID пользователя",
        example=1,
    )
    book_id: int = Field(
        ...,
        description="ID забронированной книги",
        example=2,
    )


class ReservationCreate(ReservationBase):
    """Схема бронирования для POST запроса."""

    pass


class ReservationUpdate(ReservationBase):
    """Схема бронирования для UPDATE запроса."""

    pass


class ReservationResponse(ReservationBase):
    """Схема бронирования для вывода ответа."""

    class Config:
        from_attributes = True

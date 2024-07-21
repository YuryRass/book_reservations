from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.book.model import Book
    from app.reservation.model import Reservation


class User(Base):
    """Модель пользователя."""

    first_name: Mapped[str]
    last_name: Mapped[str]
    avatar: Mapped[str]

    books: Mapped[list['Book']] = relationship(
        back_populates='author',
        cascade='all, delete',
    )

    reservations: Mapped[list["Reservation"]] = relationship(
        back_populates="user",
        cascade='all, delete',
    )

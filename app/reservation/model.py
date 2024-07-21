from typing import TYPE_CHECKING
from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base, book_genre_association

if TYPE_CHECKING:
    from app.user.model import User
    from app.book.model import Book

class Reservation(Base):
    """Модель бронирования книг."""

    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id', ondelete='CASCADE'),)
    book_id: Mapped[int] = mapped_column(ForeignKey('book.id', ondelete='CASCADE'),)

    user: Mapped["User"] = relationship(back_populates='reservations')
    book: Mapped["Book"] = relationship(back_populates='reservations')
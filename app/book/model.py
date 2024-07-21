from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base, book_genre_association

if TYPE_CHECKING:
    from app.user.model import User
    from app.genre.model import Genre


class Book(Base):
    """Модель книг."""

    title: Mapped[str]
    author: Mapped[str]
    price: Mapped[float]
    pages: Mapped[int]

    author_id: Mapped[int] = mapped_column(
        ForeignKey('user.id', ondelete='CASCADE'),
    )
    author = Mapped["User"] = relationship(back_populates='books')
    genres = Mapped[list["Genre"]] = relationship(secondary=book_genre_association, back_populates="books")

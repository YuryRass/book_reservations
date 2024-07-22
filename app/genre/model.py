from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from app.database import Base, book_genre_association

if TYPE_CHECKING:
    from app.book.model import Book


class Genre(Base):
    """Модель жанров для книг."""

    name: Mapped[str]

    books: Mapped[list["Book"]] = relationship(
        secondary=book_genre_association,
        back_populates="genres",
        cascade="all, delete",
    )

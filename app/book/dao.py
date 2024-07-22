from typing import Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.book.model import Book
from app.book.shemas import BookRead
from app.dao.base import BaseDAO
from app.database import async_session
from app.genre.model import Genre


class BookDAO(BaseDAO):
    """CRUD операции для книг."""

    model = Book

    @classmethod
    async def read_books_by_genre(cls, genre_id: int) -> list[BookRead]:
        stmt = select(Book.__table__.columns).select_from(Book).join(
            Book.genres).filter(Genre.id == genre_id)

        session: AsyncSession
        async with async_session() as session:
            result = await session.execute(stmt)
            return result.all()

    @classmethod
    async def filter_books_by_price(
        cls, min_price: float | None = None,
        max_price: float | None = None,
    ) -> list[BookRead]:
        """Получение книг с фильтрацией по цене."""
        query = select(Book.__table__.columns)
        if min_price is not None:
            query = query.filter(Book.price >= min_price)
        if max_price is not None:
            query = query.filter(Book.price <= max_price)

        session: AsyncSession
        async with async_session() as session:
            result = await session.execute(query)
            return result.all()

    @classmethod
    async def filter_books(
        cls,
        min_price: float | None = None,
        max_price: float | None = None,
        genre: str | None = None,
        author_id: int | None = None,
    ) -> Any:
        query = select(Book).options(selectinload(Book.genres)
                                     ).options(selectinload(Book.author))

        if min_price is not None:
            query = query.where(Book.price >= min_price)
        if max_price is not None:
            query = query.where(Book.price <= max_price)
        if genre is not None:
            query = query.filter(Book.genres.any(Genre.name == genre))
        if author_id is not None:
            query = query.where(Book.author_id == author_id)

        session: AsyncSession
        async with async_session() as session:
            result = await session.execute(query)
            books = result.scalars().all()

        return books

from fastapi import Query

from app.book.dao import BookDAO
from app.book.shemas import BookCreate, BookRead, BookUpdate, FilterBook
from app.exceptions import BookNotFoundException


class BookService:
    @classmethod
    async def create_book(cls, book: BookCreate) -> BookRead:
        """Создание книги."""
        return await BookDAO.add(**book.model_dump())

    @classmethod
    async def read_books(cls) -> list[BookRead]:
        """Получение всех книги."""
        return await BookDAO.read()

    @classmethod
    async def read_book(cls, book_id: int) -> BookRead:
        """Получение книги по ID."""
        book = await BookDAO.get_by_id(book_id)
        if book is None:
            raise BookNotFoundException
        return book

    @classmethod
    async def update_book(cls, book_id: int, book: BookUpdate) -> BookRead:
        """Обновление книги."""
        updated_book = await BookDAO.update(book_id, **book.model_dump())
        if updated_book is None:
            raise BookNotFoundException
        return updated_book

    @classmethod
    async def delete_book(cls, book_id: int) -> BookRead:
        """Удаление книги по ID."""
        deleted_book = await BookDAO.delete(id=book_id)
        if deleted_book is None:
            raise BookNotFoundException
        return deleted_book

    @classmethod
    async def read_books_by_author(cls, author_id: int) -> list[BookRead]:
        """Получение книг по автору."""
        books = await BookDAO.read(author_id=author_id)
        if not books:
            raise BookNotFoundException
        return books

    @classmethod
    async def read_books_by_genre(cls, genre_id: int) -> list[BookRead]:
        """Получение книг по жанру."""
        books = await BookDAO.read_books_by_genre(genre_id)
        if not books:
            raise BookNotFoundException
        return books

    @classmethod
    async def get_books(
        cls,
        min_price: float | None = Query(
            None, description="Минимальная цена книги"),
        max_price: float | None = Query(
            None, description="Максимальная цена книги"),
        genre: str | None = Query(None, description="Жанр книги"),
        author_id: int | None = Query(None, description="ID автора книги"),
    ) -> list[FilterBook]:
        """Вывод подробной информации о книгах с применением фильтрации."""
        books = await BookDAO.filter_books(
            min_price, max_price, genre, author_id,
        )
        return books

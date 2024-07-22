from typing import Any
from fastapi import APIRouter, Query

from app.exceptions import BookNotFoundException
from app.book.dao import BookDAO
from app.book.shemas import BookRead, BookCreate, BookUpdate, FilterBook


router: APIRouter = APIRouter(tags=['Books'])


@router.post("/books/", response_model=BookRead)
async def create_book(book: BookCreate) -> BookRead:
    """Создание книги."""
    return await BookDAO.add(**book.model_dump())


@router.get("/books/", response_model=list[BookRead])
async def read_books() -> list[BookRead]:
    """Получение всех книги."""
    return await BookDAO.read()


@router.get("/books/{book_id}", response_model=BookRead)
async def read_book(book_id: int) -> BookRead:
    """Получение книги по ID."""
    book = await BookDAO.get_by_id(book_id)
    if book is None:
        raise BookNotFoundException
    return book


@router.put("/books/{book_id}", response_model=BookRead)
async def update_book(book_id: int, book: BookUpdate) -> BookRead:
    """Обновление книги."""
    updated_book = await BookDAO.update(book_id, **book.model_dump())
    if updated_book is None:
        raise BookNotFoundException
    return updated_book


@router.delete("/books/{book_id}", response_model=BookRead)
async def delete_book(book_id: int) -> BookRead:
    """Удаление книги по ID."""
    deleted_book = await BookDAO.delete(id=book_id)
    if deleted_book is None:
        raise BookNotFoundException
    return deleted_book


@router.get("/users/{author_id}/books/", response_model=list[BookRead])
async def read_books_by_author(author_id: int) -> list[BookRead]:
    """Получение книг по автору."""
    books = await BookDAO.read(author_id=author_id)
    if not books:
        raise BookNotFoundException
    return books


@router.get("/genres/{genre_id}/books/", response_model=list[BookRead])
async def read_books_by_genre(genre_id: int) -> list[BookRead]:
    """Получение книг по жанру."""
    books = await BookDAO.read_books_by_genre(genre_id)
    if not books:
        raise BookNotFoundException
    return books


@router.get("/books/filter/")
async def get_books(
    min_price: float | None = Query(
        None, description="Минимальная цена книги"),
    max_price: float | None = Query(
        None, description="Максимальная цена книги"),
    genre: str | None = Query(None, description="Жанр книги"),
    author_id: int | None = Query(None, description="ID автора книги")
) -> list[FilterBook]:
    """Вывод подробной информации о книгах с применением фильтрации."""
    books = await BookDAO.filter_books(min_price, max_price, genre, author_id)
    return books

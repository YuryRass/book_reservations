from fastapi import APIRouter, Query

from app.book.service import BookService
from app.book.shemas import BookCreate, BookRead, BookUpdate, FilterBook, ReservedBook

router: APIRouter = APIRouter(tags=["Books"])


@router.post("/books/", response_model=BookRead)
async def create_book(book: BookCreate) -> BookRead:
    """Создание книги."""
    return await BookService.create_book(book)


@router.get("/books/", response_model=list[BookRead])
async def read_books() -> list[BookRead]:
    """Получение всех книги."""
    return await BookService.read_books()


@router.get("/books/{book_id}", response_model=BookRead)
async def read_book(book_id: int) -> BookRead:
    """Получение книги по ID."""
    return await BookService.read_book(book_id)


@router.put("/books/{book_id}", response_model=BookRead)
async def update_book(book_id: int, book: BookUpdate) -> BookRead:
    """Обновление книги."""
    return await BookService.update_book(book_id, book)


@router.delete("/books/{book_id}", response_model=BookRead)
async def delete_book(book_id: int) -> BookRead:
    """Удаление книги по ID."""
    return await BookService.delete_book(book_id)


@router.get("/users/{author_id}/books/", response_model=list[BookRead])
async def read_books_by_author(author_id: int) -> list[BookRead]:
    """Получение книг по автору."""
    return await BookService.read_books_by_author(author_id)


@router.get("/genres/{genre_id}/books/", response_model=list[BookRead])
async def read_books_by_genre(genre_id: int) -> list[BookRead]:
    """Получение книг по жанру."""
    return await BookService.read_books_by_genre(genre_id)


@router.get("/books/filter/")
async def get_books(
    min_price: float | None = Query(None, description="Минимальная цена книги"),
    max_price: float | None = Query(None, description="Максимальная цена книги"),
    genre: str | None = Query(None, description="Жанр книги"),
    author_id: int | None = Query(None, description="ID автора книги"),
) -> list[FilterBook]:
    """Вывод подробной информации о книгах с применением фильтрации."""
    return await BookService.get_books(min_price, max_price, genre, author_id)


@router.get("/books/reserved/", response_model=list[ReservedBook])
async def get_reserved_books(user_id: int) -> list[ReservedBook]:
    """Вывод забронированных пользователем книг."""
    return await BookService.get_reserved_books(user_id)

from pydantic import Field

from app.base.shema import MainModel
from app.genre.shemas import GenreResponse
from app.user.shemas import UserResponse


class BookBase(MainModel):
    id: int | None = Field(
        None,
        description="Уникальный идентификатор книги",
        example="1",
    )
    title: str = Field(
        ...,
        description="Название книги",
        example="Горе от ума",
    )
    price: float = Field(
        ...,
        description="Цена за книгу",
        example="129.33",
    )
    pages: int = Field(
        ...,
        description="Количество страниц в книге",
        example="123",
    )
    author_id: int = Field(
        ...,
        description="ID автора книги",
        example="1",
    )


class BookRead(BookBase):
    class Config:
        from_attributes = True


class BookCreate(BookBase):
    pass


class BookUpdate(MainModel):
    title: str | None = Field(
        None,
        description="Название книги",
        example="Горе от ума",
    )
    price: float | None = Field(
        None,
        description="Цена за книгу",
        example="129.33",
    )
    pages: int | None = Field(
        None,
        description="Количество страниц в книге",
        example="123",
    )


class FilterBook(BookBase):
    """Модель полного вывода информации и книгах."""

    genres: list[GenreResponse]
    author: UserResponse


class ReservedBook(BookRead):
    """Модель для забронированных книг"""

    user_id: int

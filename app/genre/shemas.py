from pydantic import Field

from app.base.shema import MainModel


class GenreBase(MainModel):
    """Основная схема для жанров."""
    id: int | None = Field(
        None,
        description='Уникальный идентификатор жанра',
        example='222',
    )
    name: str = Field(
        ...,
        description='Название жанра',
        example='Детектив',
    )


class GenreCreate(GenreBase):
    """Схема жанров для POST запроса."""
    pass


class GenreUpdate(GenreBase):
    """Схема жанров для UPDATE запроса."""
    pass


class GenreResponse(GenreBase):
    """Схема жанров для вывода ответа."""
    class Config:
        from_attributes = True

from pydantic import Field

from app.base.shema import MainModel


class UserBase(MainModel):
    """Основная схема для пользователя."""

    id: int | None = Field(
        None,
        description="Уникальный идентификатор пользователя",
        example="111",
    )
    first_name: str = Field(
        ...,
        description="Имя пользователя",
        example="Иван",
    )
    last_name: str = Field(
        ...,
        description="Фамилия пользователя",
        example="Иванов",
    )
    avatar: str = Field(
        "",
        description="Путь до директории с фото аватора",
        example="/path/to/image.png",
    )


class UserCreate(UserBase):
    """Схема пользователя для POST запроса."""


class UserUpdate(UserBase):
    """Схема пользователя для UPDATE запроса."""


class UserResponse(UserBase):
    """Схема пользователя для GET запроса."""

    class Config:
        from_attributes = True

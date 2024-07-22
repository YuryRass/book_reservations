from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """Основная схема для пользователя."""
    id: int | None = Field(
        None,
        description='Уникальный идентификатор пользователя',
        example='111',
    )
    first_name: str = Field(
        ...,
        description='Имя пользователя',
        example='Иван',
    )
    last_name: str = Field(
        ...,
        description="Фамилия пользователя",
        example="Иванов",
    )
    avatar: str = Field(
        "",
        description="Путь до директории с фото аватора",
        example="/path/to/image.png"
    )

    def model_dump(self, *args, **kwargs) -> dict:
        return super().model_dump(*args, exclude_none=True, **kwargs)


class UserCreate(UserBase):
    """Схема пользователя для POST запроса."""
    pass


class UserUpdate(UserBase):
    """Схема пользователя для UPDATE запроса."""
    pass


class UserResponse(UserBase):
    """Схема пользователя для GET запроса."""
    class Config:
        from_attributes = True

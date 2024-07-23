from app.exceptions import UserNotFoundException
from app.user.dao import UserDAO
from app.user.shemas import UserCreate, UserResponse, UserUpdate


class UserService:
    """Сервисный слой для пользователя."""

    @classmethod
    async def create_user(cls, user: UserCreate) -> UserResponse:
        "Создание пользователя в БД."
        return await UserDAO.add(**user.model_dump())

    @classmethod
    async def read_users(cls) -> list[UserResponse]:
        "Чтение всех пользователей из БД."
        return await UserDAO.read()

    @classmethod
    async def read_user(cls, user_id: int) -> UserResponse:
        """Чтение пользователя из БД по его ID."""
        user = await UserDAO.get_by_id(user_id)
        if user is None:
            raise UserNotFoundException
        return user

    @classmethod
    async def update_user(cls, user_id: int, user: UserUpdate) -> UserResponse:
        """Изменение пользовательских данных."""
        updated_user = await UserDAO.update(user_id, **user.model_dump())
        if updated_user is None:
            raise UserNotFoundException
        return updated_user

    @classmethod
    async def delete_user(cls, user_id: int):
        """Удаление пользователя из БД."""
        deleted_user = await UserDAO.delete(id=user_id)
        if deleted_user is None:
            raise UserNotFoundException
        return deleted_user

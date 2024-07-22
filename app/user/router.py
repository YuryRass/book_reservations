from fastapi import APIRouter

from app.exceptions import UserNotFoundException
from app.user.dao import UserDAO
from app.user.shemas import UserCreate, UserResponse, UserUpdate

router: APIRouter = APIRouter(tags=['Users'])


@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate) -> UserResponse:
    "Создание пользователя в БД."
    return await UserDAO.add(**user.model_dump())


@router.get("/users/", response_model=list[UserResponse])
async def read_users() -> list[UserResponse]:
    "Чтение всех пользователей из БД."
    return await UserDAO.read()


@router.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int) -> UserResponse:
    """Чтение пользователя из БД по его ID."""
    user = await UserDAO.get_by_id(user_id)
    if user is None:
        raise UserNotFoundException
    return user


@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate) -> UserResponse:
    """Изменение пользовательских данных."""
    updated_user = await UserDAO.update(user_id, **user.model_dump())
    if updated_user is None:
        raise UserNotFoundException
    return updated_user


@router.delete("/users/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int):
    """Удаление пользователя из БД."""
    deleted_user = await UserDAO.delete(id=user_id)
    if deleted_user is None:
        raise UserNotFoundException
    return deleted_user

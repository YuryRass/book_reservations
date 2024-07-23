from fastapi import APIRouter

from app.user.service import UserService
from app.user.shemas import UserCreate, UserResponse, UserUpdate

router: APIRouter = APIRouter(tags=["Users"])


@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate) -> UserResponse:
    "Создание пользователя в БД."
    return await UserService.create_user(user)


@router.get("/users/", response_model=list[UserResponse])
async def read_users() -> list[UserResponse]:
    "Чтение всех пользователей из БД."
    return await UserService.read_users()


@router.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int) -> UserResponse:
    """Чтение пользователя из БД по его ID."""
    return await UserService.read_user(user_id)


@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserUpdate) -> UserResponse:
    """Изменение пользовательских данных."""
    return await UserService.update_user(user_id, user)


@router.delete("/users/{user_id}", response_model=UserResponse)
async def delete_user(user_id: int):
    """Удаление пользователя из БД."""
    return await UserService.delete_user(user_id)

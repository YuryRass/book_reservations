from app.dao.base import BaseDAO
from app.user.model import User


class UserDAO(BaseDAO):
    """CRUD операции для пользователя."""

    model = User

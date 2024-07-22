"""Различные HTTP-ошибки"""

from fastapi import HTTPException, status


class MainException(HTTPException):
    """Базовое исключение для приложения."""
    status_code = 500
    detail = ''

    def __init__(self) -> None:
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserNotFoundException(MainException):
    """Исключение: пользователь не найден."""
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'User not found'

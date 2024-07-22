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


class GenreNotFoundException(MainException):
    """Исключение: жанр не найден."""
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Genre not found'


class BookNotFoundException(MainException):
    """Исключение: книга не найдена."""
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Book not found'


class ReservationNotFoundException(MainException):
    """Исключение: бронь не найдена."""
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'Reservation not found'


class ExistingReservationException(MainException):
    """Бронь для книги уже существует."""
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'This book is already reserved for the specified dates.'

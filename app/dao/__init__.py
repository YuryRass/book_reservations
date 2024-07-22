from typing import TypeVar

from app.book.model import Book
from app.genre.model import Genre
from app.reservation.model import Reservation
from app.user.model import User

ModelType = TypeVar("ModelType", Book, User, Reservation, Genre)

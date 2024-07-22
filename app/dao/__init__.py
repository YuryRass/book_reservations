from typing import TypeVar
from app.book.model import Book
from app.user.model import User
from app.reservation.model import Reservation
from app.genre.model import Genre

ModelType = TypeVar('ModelType', Book, User, Reservation, Genre)
from app.dao.base import BaseDAO
from app.genre.model import Genre


class GenreDAO(BaseDAO):
    """CRUD операции для жанров книг."""

    model = Genre

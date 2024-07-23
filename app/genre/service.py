from app.exceptions import GenreNotFoundException
from app.genre.dao import GenreDAO
from app.genre.shemas import GenreCreate, GenreResponse, GenreUpdate


class GenreService:
    """Сервисный слой жанров."""

    @classmethod
    async def create_genre(cls, genre: GenreCreate) -> GenreResponse:
        "Создание нового жанра в БД."
        return await GenreDAO.add(**genre.model_dump())

    @classmethod
    async def read_genres(cls) -> list[GenreResponse]:
        "Чтение всех жанров из БД."
        return await GenreDAO.read()

    @classmethod
    async def read_genre(cls, genre_id: int) -> GenreResponse:
        """Чтение жанра из БД по его ID."""
        genre = await GenreDAO.get_by_id(genre_id)
        if genre is None:
            raise GenreNotFoundException
        return genre

    @classmethod
    async def update_genre(
        cls, genre_id: int, genre: GenreUpdate
    ) -> GenreResponse:
        """Изменение жанра по его ID."""
        updated_genre = await GenreDAO.update(genre_id, **genre.model_dump())
        if updated_genre is None:
            raise GenreNotFoundException
        return updated_genre

    @classmethod
    async def delete_genre(cls, genre_id: int):
        """Удаление жанра из БД."""
        deleted_genre = await GenreDAO.delete(id=genre_id)
        if deleted_genre is None:
            raise GenreNotFoundException
        return deleted_genre

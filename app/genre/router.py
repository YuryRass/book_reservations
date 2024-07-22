from fastapi import APIRouter

from app.exceptions import GenreNotFoundException
from app.genre.dao import GenreDAO
from app.genre.shemas import GenreCreate, GenreUpdate, GenreResponse


router: APIRouter = APIRouter(tags=['Genres'])


@router.post("/genres/", response_model=GenreResponse)
async def create_genre(genre: GenreCreate) -> GenreResponse:
    "Создание нового жанра в БД."
    return await GenreDAO.add(**genre.model_dump())


@router.get("/genres/", response_model=list[GenreResponse])
async def read_genres() -> list[GenreResponse]:
    "Чтение всех жанров из БД."
    return await GenreDAO.read()


@router.get("/genres/{genre_id}", response_model=GenreResponse)
async def read_genre(genre_id: int) -> GenreResponse:
    """Чтение жанра из БД по его ID."""
    genre = await GenreDAO.get_by_id(genre_id)
    if genre is None:
        raise GenreNotFoundException
    return genre


@router.put("/genres/{genre_id}", response_model=GenreResponse)
async def update_genre(genre_id: int, genre: GenreUpdate) -> GenreResponse:
    """Изменение жанра по его ID."""
    updated_genre = await GenreDAO.update(genre_id, **genre.model_dump())
    if updated_genre is None:
        raise GenreNotFoundException
    return updated_genre


@router.delete("/genres/{genre_id}", response_model=GenreResponse)
async def delete_genre(genre_id: int):
    """Удаление жанра из БД."""
    deleted_genre = await GenreDAO.delete(id=genre_id)
    if deleted_genre is None:
        raise GenreNotFoundException
    return deleted_genre

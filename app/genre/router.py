from fastapi import APIRouter

from app.genre.service import GenreService
from app.genre.shemas import GenreCreate, GenreResponse, GenreUpdate

router: APIRouter = APIRouter(tags=["Genres"])


@router.post("/genres/", response_model=GenreResponse)
async def create_genre(genre: GenreCreate) -> GenreResponse:
    "Создание нового жанра в БД."
    return await GenreService.create_genre(genre)


@router.get("/genres/", response_model=list[GenreResponse])
async def read_genres() -> list[GenreResponse]:
    "Чтение всех жанров из БД."
    return await GenreService.read_genres()


@router.get("/genres/{genre_id}", response_model=GenreResponse)
async def read_genre(genre_id: int) -> GenreResponse:
    """Чтение жанра из БД по его ID."""
    return await GenreService.read_genre(genre_id)


@router.put("/genres/{genre_id}", response_model=GenreResponse)
async def update_genre(genre_id: int, genre: GenreUpdate) -> GenreResponse:
    """Изменение жанра по его ID."""
    return await GenreService.update_genre(genre_id, genre)


@router.delete("/genres/{genre_id}", response_model=GenreResponse)
async def delete_genre(genre_id: int):
    """Удаление жанра из БД."""
    return await GenreService.delete_genre(genre_id)

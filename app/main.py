from fastapi import FastAPI

from app.user.router import router as dish_router
from app.genre.router import router as genre_router
from app.book.router import router as book_router


description = """FastAPI приложение для работы с книгами"""

tags_metadata = [
    {
        'name': 'Users',
        'description': 'CRUD операции с пользователями',
    },
    {
        'name': 'Genres',
        'description': 'CRUD операции с жанрами',
    },
    {
        'name': 'Books',
        'description': 'CRUD операции с книгами',
    }
]


app: FastAPI = FastAPI(
    title='FastAPI book reservations API',
    description=description,
    version='1.0.0',
    terms_of_service='http://example.com/terms/',
    contact={
        'name': 'Support Team',
        'url': 'http://example.com/contact/',
        'email': 'support@example.com',
    },
    license_info={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    openapi_tags=tags_metadata,
)

app.include_router(dish_router)
app.include_router(genre_router)
app.include_router(book_router)
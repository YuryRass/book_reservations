"""add test data

Revision ID: a556df013cca
Revises: e8e92c001391
Create Date: 2024-07-22 00:11:32.954836

"""
from datetime import datetime, timedelta
from typing import Sequence, Union

from alembic import op
from sqlalchemy.orm import Session

from app.book.model import Book
from app.genre.model import Genre
from app.reservation.model import Reservation
from app.user.model import User
from app.database import book_genre_association


# revision identifiers, used by Alembic.
revision: str = 'a556df013cca'
down_revision: Union[str, None] = 'e8e92c001391'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Добавление тестовых данных в БД."""
    # Добавление тестовых пользователей
    user1 = User(
        first_name="Иван",
        last_name="Иванов",
        avatar="path/to/avatar1.png",
    )

    user2 = User(
        first_name="Мария",
        last_name="Петрова",
        avatar="path/to/avatar2.png",
    )

    # Добавление тестовых жанров
    genre1 = Genre(name="Фантастика")
    genre2 = Genre(name="Научная")
    genre3 = Genre(name="Драма")

    # Заполнение БД
    bind = op.get_bind()
    session = Session(bind)

    # Вставка пользователей
    session.add_all([user1, user2, genre1, genre2, genre3])

    # Синхронизация изменений
    session.flush()

    # Добавление тестовых книг
    book1 = Book(
        title="Книга 1",
        price=299.99,
        pages=350,
        author_id=user1.id,  # ID пользователя
        genres=[genre1, genre3],
    )

    book2 = Book(
        title="Книга 2",
        price=399.99,
        pages=450,
        author_id=user2.id,  # ID пользователя
        genres=[genre2],
    )

    session.add_all([book1, book2])

    # Синхронизация
    session.flush()

    # Добавление тестовых бронирований
    reservation1 = Reservation(
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=7),
        user_id=user1.id,  # ID пользователя
        book_id=book1.id,   # ID книги
    )

    reservation2 = Reservation(
        start_date=datetime.now(),
        end_date=datetime.now() + timedelta(days=5),
        user_id=user2.id,  # ID пользователя
        book_id=book2.id,   # ID книги
    )

    # Вставка бронирований
    session.add_all([reservation1, reservation2])

    # Окончательное сохранение изменений в базе данных
    session.commit()
    # Закрытие сессии
    session.close()


def downgrade() -> None:
    """Удаление всех данных из таблиц."""

    bind = op.get_bind()
    session = Session(bind)

    # many-to-many
    session.query(book_genre_association).delete()
    # Удаление всех жанров
    session.query(Genre).delete()
    # Удаление всех пользователей
    session.query(User).delete()
    # Удаление всех бронирований
    session.query(Reservation).delete()
    # Удаление всех книг
    session.query(Book).delete()
    # Сохранение изменений в базе данных
    session.commit()
    # Закрытие сессии
    session.close()

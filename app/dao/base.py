"""Основной DAO (Data Access Object)."""

from typing import Any, Generic

from sqlalchemy import delete, insert, select, update
from sqlalchemy.engine.row import Row
from sqlalchemy.ext.asyncio import AsyncSession

from app.dao import ModelType
from app.database import async_session


class BaseDAO(Generic[ModelType]):
    """Класс, описывающий основные CRUD операции для моделей."""

    model: type[ModelType]

    @classmethod
    async def get_by_id(cls, model_id: int) -> Row | None:
        """Получение записи в модели по ее ID."""
        session: AsyncSession
        async with async_session() as session:
            stmt = select(cls.model.__table__.columns).where(
                cls.model.id == model_id)
            result = await session.execute(stmt)
            return result.one_or_none()

    @classmethod
    async def read(cls, **kwargs: Any) -> Any:
        """Чтение данных из модели."""
        session: AsyncSession
        async with async_session() as session:
            stmt = select(cls.model.__table__.columns).select_from(
                cls.model).filter_by(**kwargs)
            result = await session.execute(stmt)
            return result.all()

    @classmethod
    async def add(cls, **data) -> Row:
        """Добавление записи в модель."""
        assert cls.model is not None
        stmt = insert(cls.model).values(
            **data).returning(cls.model.__table__.columns)
        session: AsyncSession
        async with async_session() as session:
            result = await session.execute(stmt)
            await session.commit()
            return result.one()

    @classmethod
    async def update(cls, model_id: int, **data) -> Row | None:
        """Изменение записи в модели."""
        assert cls.model is not None
        stmt = (
            update(cls.model)
            .where(cls.model.id == model_id)
            .values(**data)
            .returning(cls.model.__table__.columns)
        )
        session: AsyncSession
        async with async_session() as session:
            result = await session.execute(stmt)
            await session.commit()
            return result.one_or_none()

    @classmethod
    async def delete(cls, **kwargs) -> Row | None:
        """Удаление записи из модели."""
        assert cls.model is not None
        stmt = delete(cls.model).filter_by(
            **kwargs).returning(cls.model.__table__.columns)

        session: AsyncSession
        async with async_session() as session:
            result = await session.execute(stmt)
            await session.commit()
            return result.one_or_none()

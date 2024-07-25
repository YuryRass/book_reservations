from typing import Any

from aioredis import ConnectionPool, Redis

from app.config import get_settings

settings = get_settings()


class AsyncRedisCacher:
    """Нереляционная база данных Redis."""

    async_pool: ConnectionPool = ConnectionPool.from_url(settings.REDIS_URL)
    pool: ConnectionPool = ConnectionPool.from_url(settings.REDIS_URL)

    @classmethod
    def get_cacher(cls) -> Redis:
        """Получение асинхр. Redis."""
        return Redis(connection_pool=cls.async_pool)


class RedisClient:
    """Операции добавления, чтения и удаления в Redis."""

    _redis: Redis = AsyncRedisCacher.get_cacher()

    assert _redis is not None

    @classmethod
    async def set(cls, key: Any, value: Any) -> None:
        """Устанаваливает занчение по ключу."""
        await cls._redis.set(key, value)

    @classmethod
    async def pop(cls, key: Any) -> Any:
        """Получение значения по ключу и удаление найденной записи."""
        value = await cls._redis.get(key)
        if value is not None:
            await cls._redis.delete(key)
        return value

    @classmethod
    async def delete(cls, key: Any) -> None:
        """Удаление по ключу."""
        await cls._redis.delete(key)

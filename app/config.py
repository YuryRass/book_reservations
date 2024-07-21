from typing import Any
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Настройка приложения."""

    # данные для БД PostgreSQL
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL(self) -> str:
        """URL адрес базы данных."""
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


    model_config = SettingsConfigDict(env_file=".env")


def get_settings(**kwargs: Any) -> Settings:
    return Settings(**kwargs)
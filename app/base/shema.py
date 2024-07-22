from pydantic import BaseModel


class MainModel(BaseModel):
    """Базовая схема."""

    def model_dump(self, *args, **kwargs) -> dict:
        return super().model_dump(*args, exclude_none=True, **kwargs)

from celery import Celery

from app.config import get_settings

settings = get_settings()

celery = Celery(
    'tasks',
    broker=settings.REDIS_URL,
    include=['app.tasks.tasks'],
)

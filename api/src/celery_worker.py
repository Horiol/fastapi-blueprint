from celery import Celery
from src.constants import REDIS_CELERY_DB

# Configure Celery application
worker = Celery(
    "fastapi_celery",
    broker=f"redis://localhost:6379/{REDIS_CELERY_DB}",
    backend=f"redis://localhost:6379/{REDIS_CELERY_DB}",
    # include=["src.celery_app"],
)

worker.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    worker_concurrency=2,
)

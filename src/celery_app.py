from celery import Celery
from typing import Any, Dict

# Configure Celery application
celery_app = Celery(
    "fastapi_celery", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0", include=["src.celery_app"]
)

# Optional configuration settings
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    worker_concurrency=2,
)


@celery_app.task(name="example_task")
def example_task(word: str) -> Dict[str, Any]:
    """
    Example Celery task that counts the number of characters in a word.

    Args:
        word: The input word to process

    Returns:
        A dictionary containing the word and its character count
    """
    return {"word": word, "character_count": len(word)}


# For direct invocation
if __name__ == "__main__":
    celery_app.start()

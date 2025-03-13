from fastapi import APIRouter

from src.celery_app import example_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/example", status_code=202)
async def create_task(word: str):
    task = example_task.delay(word=word)
    return {"task_id": task.id, "status": task.status, "message": "Task submitted successfully"}

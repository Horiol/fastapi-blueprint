from fastapi import APIRouter

from src.celery_worker import worker

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/example", status_code=202)
async def create_task(word: str):
    task = worker.send_task("example_task", args=[word])
    return {
        "task_id": task.id,
        "status": task.status,
        "message": "Task submitted successfully",
    }

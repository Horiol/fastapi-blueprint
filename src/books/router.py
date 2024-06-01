from fastapi import APIRouter, Depends

from src.database import get_session

from . import service
from .models import Book, BookBase

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[Book])
def get(db=Depends(get_session)):
    return service.get(db)


@router.post("/", response_model=Book)
def post(payload: BookBase, db=Depends(get_session)):
    return service.create(db, payload)

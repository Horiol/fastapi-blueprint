from fastapi import APIRouter, Depends
from database import get_session
from .service import Service
from . import models

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[models.Book])
def get(db=Depends(get_session)):
    return Service.get(db)


@router.post("/", response_model=models.Book)
def post(payload: models.BookBase, db=Depends(get_session)):
    return Service.create(db, payload)

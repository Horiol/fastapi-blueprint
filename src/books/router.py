from fastapi import APIRouter, Depends

from database import get_session

from . import models, service

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=list[models.Book])
def get(db=Depends(get_session)):
    return service.get(db)


@router.post("/", response_model=models.Book)
def post(payload: models.BookBase, db=Depends(get_session)):
    return service.create(db, payload)

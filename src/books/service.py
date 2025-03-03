from sqlmodel import select
from . import models


def get(db):
    return db.scalars(select(models.Book)).all()


def create(db, payload: models.BookBase):
    db_book = models.Book.model_validate(payload)

    db.add(db_book)
    db.flush()

    return db_book

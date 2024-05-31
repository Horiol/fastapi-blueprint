from sqlmodel import select
from . import models


class Service:
    @classmethod
    def get(cls, db):
        return db.execute(select(models.Book)).all()

    @classmethod
    def create(cls, db, payload: models.BookBase):
        db_book = models.Book.model_validate(payload)

        db.add(db_book)
        db.flush()

        return db_book

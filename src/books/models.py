from sqlmodel import SQLModel, Field


class BookBase(SQLModel):
    title: str
    author: str


class Book(BookBase, table=True):
    id: int = Field(default=None, primary_key=True)

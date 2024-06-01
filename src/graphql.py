# from src.books.models import Book
import strawberry
from strawberry.asgi import GraphQL


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    books: list[Book]


schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

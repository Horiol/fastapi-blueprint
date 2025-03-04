import strawberry
from strawberry.asgi import GraphQL
from src.database import get_db_graphql
from src.books.service import get as get_books


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    @strawberry.field
    async def books(self) -> list[Book]:
        db = get_db_graphql()
        return get_books(db)


schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

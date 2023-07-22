from strawberry.asgi import GraphQL
import strawberry
from db import get_session
from typing import Optional
from models import tasks
from sqlalchemy import select


@strawberry.type
class Location:
    id: strawberry.ID
    name: str

    @classmethod
    def marshal(cls, model: tasks.Location) -> "Location":
        return cls(id=strawberry.ID(str(model.id)), name=model.name)


@strawberry.type
class Task:
    id: strawberry.ID
    name: str
    location: Optional[Location] = None

    @classmethod
    def marshal(cls, model: tasks.Task) -> "Task":
        return cls(
            id=strawberry.ID(str(model.id)),
            name=model.name,
            location=Location.marshal(model.location) if model.location else None,
        )


@strawberry.type
class Query:
    @strawberry.field
    async def tasks(self) -> list[Task]:
        async with get_session() as s:
            sql = select(tasks.Task).order_by(tasks.Task.name)
            db_tasks = (await s.execute(sql)).scalars().unique().all()
        return [Task.marshal(task) for task in db_tasks]

    @strawberry.field
    async def locations(self) -> list[Location]:
        async with get_session() as s:
            sql = select(tasks.Location).order_by(tasks.Location.name)
            db_locations = (await s.execute(sql)).scalars().unique().all()
        return [Location.marshal(loc) for loc in db_locations]


schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

import uvicorn
from fastapi import FastAPI

from src.graphql import graphql_app
from src.books.router import router as books_router
from src.tasks.router import router as tasks_router
from src.admin import init_admin_page
from src.faststream_worker import router as faststream_router

app = FastAPI()


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "OK"}


app.add_route("/graphql", graphql_app)
app.include_router(books_router)
app.include_router(tasks_router)
app.include_router(faststream_router)

init_admin_page(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

import uvicorn
from routes.graphql import graphql_app
from fastapi import FastAPI

from books.router import router as books_router

app = FastAPI()


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "OK"}


app.add_route("/graphql", graphql_app)
app.include_router(books_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

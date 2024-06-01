import uvicorn
from fastapi import FastAPI

from src.books.router import router as books_router
from src.admin import init_admin_page

app = FastAPI()


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "OK"}


app.include_router(books_router)

init_admin_page(app)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

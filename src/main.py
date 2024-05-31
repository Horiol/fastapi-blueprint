from fastapi import FastAPI
import uvicorn

from books.router import router as books_router

app = FastAPI()


@app.get("/healthz")
async def healthz():
    return {"status": "OK"}


app.include_router(books_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

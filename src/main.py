import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/healthz")
async def healthz() -> dict[str, str]:
    return {"status": "OK"}


@app.get("/another_endpoint")
async def another_endpoint() -> dict[str, str]:
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/healthz")
async def root(request: Request):
    return {"status": "OK"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
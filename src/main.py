from fastapi import FastAPI
import uvicorn
from routes.graphql import graphql_app

app = FastAPI()


@app.get("/healthz")
async def healthz():
    return {"status": "OK"}


app.add_route("/graphql", graphql_app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

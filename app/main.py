from fastapi import Depends, FastAPI
from routers import task

app = FastAPI()


app.include_router(task.router)


@app.get("/")
async def root():
    return {"msg": "Hello World"}
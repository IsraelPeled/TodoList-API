from fastapi import FastAPI
from src.tasks.router import task_router

version = "v1"

app = FastAPI(
    title= "TODO List",
    description= "A REST API for TODO list application",
    version= version,
    docs_url=f"/api/{version}/docs",
    redoc_url=f"/api/{version}/redoc",
    contact={
        "name": "Israel Peled",
        "email": "israelpeled3@gmail.com"
    },
    openapi_url=f"/api/{version}/openapi.json"
)

app.include_router(router=task_router, prefix=f"/api/{version}/tasks")
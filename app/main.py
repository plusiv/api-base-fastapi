from app.core.settings import env
from app.routers.v1 import api as v1, ROUTE_PREFIX as v1_prefix
from fastapi import FastAPI
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI()
app.include_router(v1.router, prefix=v1_prefix)

# Health Check
@app.get("/ping", tags=["Health Check"])
async def ping():
    return "pong"

register_tortoise(
    app=app,
    config=env.TORTOISE_ORM,
    add_exception_handlers=True,
)

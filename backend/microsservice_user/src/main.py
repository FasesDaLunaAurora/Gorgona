from fastapi import FastAPI

app = FastAPI()

from src.routers.user_routers import user_router

app.include_router(user_router)


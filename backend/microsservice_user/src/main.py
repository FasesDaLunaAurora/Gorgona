from fastapi import FastAPI

app = FastAPI()

from src.routers.auth_routers import auth_router

app.include_router(auth_router)


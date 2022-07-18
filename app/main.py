"""Main script for app."""
from fastapi import FastAPI

from app.routes.question import router

app = FastAPI()

app.include_router(router, prefix='/v1')

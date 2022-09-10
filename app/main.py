"""Main script for app."""
from fastapi import FastAPI

from app.api.api import api_router

app = FastAPI()

app.include_router(api_router, prefix='/v1')

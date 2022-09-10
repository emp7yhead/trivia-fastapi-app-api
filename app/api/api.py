"""All API endpoints."""
from fastapi import APIRouter

from app.api.endpoints import ping, question

api_router = APIRouter()
api_router.include_router(ping.router, prefix='/ping', tags=['ping'])
api_router.include_router(question.router, prefix='', tags=['question'])

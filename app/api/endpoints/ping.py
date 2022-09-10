"""Ping endpoint."""
from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def ping() -> str:
    """Ping endpoint."""
    return 'Trivia app. Version 0.1'

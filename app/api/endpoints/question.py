"""Define endpoints for API."""

from fastapi import APIRouter

router = APIRouter(prefix='/question')


@router.get('/')
async def get_all_questions():
    """Get all questions."""
    return {'world': 'hello'}

from fastapi import APIRouter

from app.ai.schema import (
    AISuggestionRequest,
    AISuggestionResponse
)

from app.ai.service import suggest_task

router = APIRouter()


@router.post(
    "/ai/suggest",
    response_model=AISuggestionResponse
)
def ai_suggest(request: AISuggestionRequest):

    return suggest_task(request.prompt)
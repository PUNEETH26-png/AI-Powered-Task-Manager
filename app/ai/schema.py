from pydantic import BaseModel

class AISuggestionRequest(BaseModel):
    prompt: str


class AISuggestionResponse(BaseModel):
    title: str
    description: str
    priority: str
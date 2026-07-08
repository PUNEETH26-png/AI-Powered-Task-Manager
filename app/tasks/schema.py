from datetime import date
from typing import Literal
from pydantic import ConfigDict,BaseModel
class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: date
    priority: Literal["Low", "Medium", "High"]


class TaskUpdate(BaseModel):
    title: str
    description: str
    due_date: date
    priority: Literal["Low", "Medium", "High"]
    status: Literal["To Do", "In Progress", "Done"]


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    due_date: date
    priority: str
    status: str

    model_config = ConfigDict(from_attributes=True)
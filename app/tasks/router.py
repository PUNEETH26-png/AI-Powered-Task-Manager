from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.tasks.schema import TaskCreate, TaskResponse
from app.tasks.service import create_task,get_all_tasks
from app.tasks.service import update_task
from app.tasks.schema import TaskUpdate
from app.tasks.service import delete_task
router = APIRouter()


@router.post("/tasks", response_model=TaskResponse)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(
        db=db,
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        priority=task.priority,
        user_id=1
    )

@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return get_all_tasks(db)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def edit_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):
    return update_task(
        db=db,
        task_id=task_id,
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        priority=task.priority,
        status=task.status
    )

@router.delete("/tasks/{task_id}")
def remove_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    return delete_task(db, task_id)
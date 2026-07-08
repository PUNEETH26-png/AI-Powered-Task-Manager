from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from app.database.models import Task
from app.database.models import Task
from fastapi import HTTPException

def create_task(
    db: Session,
    title: str,
    description: str,
    due_date,
    priority: str,
    user_id: int
):
    task = Task(
        title=title,
        description=description,
        due_date=due_date,
        priority=priority,
        status="To Do",
        user_id=user_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_all_tasks(db: Session):
    return db.query(Task).all()

def update_task(
    db: Session,
    task_id: int,
    title: str,
    description: str,
    due_date,
    priority: str,
    status: str
):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.title = title
    task.description = description
    task.due_date = due_date
    task.priority = priority
    task.status = status

    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return {
        "message": "Task deleted successfully"
    }
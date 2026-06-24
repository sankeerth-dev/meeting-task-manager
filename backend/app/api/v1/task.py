from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.task import (
    TaskCreate,
    TaskResponse
)

from app.services.task import TaskService


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post(
    "/",
    response_model=TaskResponse
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return TaskService.create_task(
        db,
        task
    )


@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_tasks(
    db: Session = Depends(get_db)
):
    return TaskService.get_tasks(db)


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task_by_id(
    task_id: int,
    db: Session = Depends(get_db)
):
    return TaskService.get_task_by_id(
        db,
        task_id
    )
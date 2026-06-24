from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.task import Task
from app.models.user import User
from app.models.meeting import Meeting

from app.schemas.task import TaskCreate


class TaskService:

    @staticmethod
    def create_task(
        db: Session,
        task_data: TaskCreate
    ):

        assignee = (
            db.query(User)
            .filter(User.id == task_data.assignee_id)
            .first()
        )

        if not assignee:
            raise HTTPException(
                status_code=404,
                detail="Assignee not found"
            )

        assigner = (
            db.query(User)
            .filter(User.id == task_data.assigned_by)
            .first()
        )

        if not assigner:
            raise HTTPException(
                status_code=404,
                detail="Assigner not found"
            )

        meeting = (
            db.query(Meeting)
            .filter(Meeting.id == task_data.meeting_id)
            .first()
        )

        if not meeting:
            raise HTTPException(
                status_code=404,
                detail="Meeting not found"
            )

        task = Task(
            title=task_data.title,
            description=task_data.description,
            assignee_id=task_data.assignee_id,
            assigned_by=task_data.assigned_by,
            meeting_id=task_data.meeting_id
        )

        try:
            db.add(task)

            db.commit()

            db.refresh(task)

            return task

        except Exception:
            db.rollback()
            raise

    @staticmethod
    def get_tasks(
        db: Session
    ):
        return db.query(Task).all()

    @staticmethod
    def get_task_by_id(
        db: Session,
        task_id: int
    ):
        task = (
            db.query(Task)
            .filter(Task.id == task_id)
            .first()
        )

        if not task:
            raise HTTPException(
                status_code=404,
                detail="Task not found"
            )

        return task
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    TIMESTAMP,
    ForeignKey
)

from sqlalchemy.sql import func

from app.db.database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    title = Column(String(255))

    description = Column(Text)

    status = Column(String(20))

    assignee_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    assigned_by = Column(
        Integer,
        ForeignKey("users.id")
    )

    meeting_id = Column(
        Integer,
        ForeignKey("meetings.id")
    )

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    completed_at = Column(TIMESTAMP)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.schemas.meeting import (
    MeetingCreate,
    MeetingResponse
)

from app.services.meeting import MeetingService

router = APIRouter(
    prefix="/meetings",
    tags=["Meetings"]
)


@router.post(
    "/",
    response_model=MeetingResponse
)
def create_meeting(
    meeting: MeetingCreate,
    db: Session = Depends(get_db)
):
    return MeetingService.create_meeting(
        db,
        meeting
    )

@router.get(
    "/",
    response_model=list[MeetingResponse]
)
def get_meetings(
    db: Session = Depends(get_db)
):
    return MeetingService.get_meetings(db)

@router.get("/{meeting_id}")
def get_meeting_by_id(
    meeting_id: int,
    db: Session = Depends(get_db)
):
    return MeetingService.get_meeting_by_id(db, meeting_id)
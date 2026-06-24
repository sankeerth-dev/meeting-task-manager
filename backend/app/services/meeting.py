from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.meeting import Meeting
from app.models.user import User

from app.schemas.meeting import MeetingCreate


class MeetingService:

    @staticmethod
    def create_meeting(
        db: Session,
        meeting_data: MeetingCreate
    ):

        uploader = (
            db.query(User)
            .filter(
                User.id == meeting_data.uploaded_by
            )
            .first()
        )

        if not uploader:
            raise HTTPException(
                status_code=404,
                detail="Uploader not found"
            )

        meeting = Meeting(
            title=meeting_data.title,
            transcript=meeting_data.transcript,
            uploaded_by=meeting_data.uploaded_by
        )

        try:
            db.add(meeting)

            db.commit()

            db.refresh(meeting)

            return meeting

        except Exception:
            db.rollback()
            raise
    
    @staticmethod
    def get_meetings(
        db: Session
    ):
        return db.query(Meeting).all()
    
    @staticmethod
    def get_meeting_by_id(
        db: Session,
        meeting_id: int
    ):
        print("DEBUG MEETING ID:", meeting_id)

        meeting = (
            db.query(Meeting)
            .filter(Meeting.id == meeting_id)
            .first()
        )



        print("DEBUG MEETING:", meeting)

        if not meeting:
            raise HTTPException(
                status_code=404,
                detail="Meeting not found"
            )

        return meeting
from pydantic import BaseModel
from datetime import datetime


class MeetingCreate(BaseModel):
    title: str
    transcript: str
    uploaded_by: int


class MeetingResponse(BaseModel):
    id: int
    title: str
    transcript: str
    uploaded_by: int
    created_at: datetime

    class Config:
        from_attributes = True
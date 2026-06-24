from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import UserCreate
from app.services.user import UserService
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    return UserService.create_user(
        db,
        user
    )


@router.get("/")
def get_users(
    db: Session = Depends(get_db)
):
    return UserService.get_users(db)

@router.get("/{user_id}")
def get_users_id(
    user_id: int,
    db: Session = Depends(get_db)
):
    return UserService.get_user_by_id(db, user_id)
    
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from domain.models.models import UserCreate, UserResponse, UserUpdate
from repositories.user_repository import UserRepository
from services.user_service import UserService

users_router = APIRouter()

user_repository = UserRepository()
user_service = UserService(user_repository)

@users_router.post("/users/", response_model=UserResponse, status_code=201)
def save_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return user_service.save_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@users_router.get("/users/{user_id}", response_model=UserResponse)
def find_user_by_id(user_id: str, db: Session = Depends(get_db)):
    return user_service.find_user_by_id(db, user_id)


@users_router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: str, user: UserUpdate, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, user)

@users_router.delete("/users/{user_id}", status_code=204)
def delete_user_by_id(user_id: str, db: Session = Depends(get_db)):
    user_service.delete_user_by_id(db, user_id)
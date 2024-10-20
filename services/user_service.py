import bcrypt
from sqlalchemy.orm import Session
from fastapi import HTTPException

from domain.models.models import UserCreate, UserEntity, UserResponse
from repositories.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def save_user(self, db: Session, user_create: UserCreate):
        # Encriptar la contraseña
        hashed_password = bcrypt.hashpw(user_create.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        user = UserEntity(
            name=user_create.name,
            email=user_create.email,
            password=hashed_password
        )
        return self.user_repository.save_user(db, user)
    
    def find_user_by_id(self, db: Session, user_id: str):
        user = self.user_repository.find_user_by_id(db, user_id)
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        return UserResponse(name=user.name, email=user.email)
        
    def delete_user_by_id(self, db: Session, user_id: str):
        user = self.user_repository.find_user_by_id(db, user_id)
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        self.user_repository.delete_user_by_id(db, user_id)
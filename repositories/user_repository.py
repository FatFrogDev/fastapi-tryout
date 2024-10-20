from sqlalchemy.orm import Session
from domain.models.models import UserEntity

class UserRepository:

    def save_user(self, db:Session, user: UserEntity):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    def find_user_by_id(self, db: Session, user_id: str):
        return db.query(UserEntity).filter(UserEntity.user_id == user_id).first()
    
    def delete_user_by_id(self, db: Session, user_id: str):
        user = db.query(UserEntity).filter(UserEntity.user_id == user_id).first()
        db.delete(user)
        db.commit()
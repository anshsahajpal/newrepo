import uuid
from user_management.models.user import User
from sqlalchemy.orm import Session
from user_management.schemas import user
from user_management.security import get_password_hash


def create_user(data: user.CreateUser, db: Session) -> uuid.UUID:
    new_user = User()
    new_user.id = uuid.uuid4()
    new_user.email = data.email
    new_user.username = data.email
    new_user.password_hash = get_password_hash(data.password.get_secret_value())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user.id


def list_users(db: Session):
    return db.query(User).all()


def get_user(user_id: uuid.UUID, db: Session):
    usr = db.query(User).filter(User.id == user_id).first()
    return usr


def get_user_by_email(email: str, db: Session):
    usr = db.query(User).filter(User.email == email).first()
    return usr


def delete_user(user_id: uuid.UUID, db: Session):
    user_to_delete = db.query(User).filter(User.id == user_id).first()
    if user_to_delete:
        db.delete(user_to_delete)
        db.commit()

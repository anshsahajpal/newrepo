import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from user_management.db import (get_db)
from user_management.schemas.user import GetUser
from typing import List
from user_management.operations import user as user_ops
from user_management.auth import get_current_user


user_router = APIRouter(prefix="/user")


@user_router.get("")
def list_users(db: Session = Depends(get_db), current_user=Depends(get_current_user)) -> List[GetUser]:
    return user_ops.list_users(db)


@user_router.get("/{id}")
def get_user_by_id(id: str, db: Session = Depends(get_db)) -> GetUser:
    return user_ops.get_user(uuid.UUID(id), db)


@user_router.delete("/{id}")
def del_user(id: str, db: Session = Depends(get_db)):
    user_ops.delete_user(uuid.UUID(id), db)
    return ""



from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from user_management.db import get_db
from sqlalchemy.orm import Session
from user_management.operations import user as user_ops
from user_management.models.user import User
from user_management.schemas.user import CreateUser
from user_management.auth import get_current_user, create_access_token
from user_management.schemas.user import GetUser
from user_management import security

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/login")
async def login(form_data:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user: User = user_ops.get_user_by_email(form_data.username, db)
    if not user or not security.verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=" Invalid credentials")
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token":access_token, "token_type": "bearer"}


@auth_router.post("/register")
async def register(data: CreateUser, db: Session = Depends(get_db)):
    uid = user_ops.create_user(data,db)
    return str(uid)


@auth_router.get("/validate")
async def validate(current_user: GetUser=Depends(get_current_user)) -> GetUser:
    return Response(status_code=status.HTTP_200_OK, headers={"X-User-ID": str(current_user.id)})
    

from fastapi import APIRouter, Depends, status, Body, Header, HTTPException
from sqlalchemy.orm import Session
from ..schemas import UserSignUp, UserLogin
from ..database import get_db
from ..crud import auth
from ..config.response import response_data
from datetime import datetime

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def sign_up(user: UserSignUp = Body(), db: Session = Depends(get_db)):
    new_user = auth.sign_up(db=db, user=user)
    if new_user is None:
        return response_data(
            status.HTTP_409_CONFLICT, "Email already exists!", datetime.now(), ""
        )
    return response_data(
        status.HTTP_201_CREATED, "Sign up successful!", datetime.now(), ""
    )


@router.post("/login", status_code=status.HTTP_200_OK)
def login(user: UserLogin = Body(), db: Session = Depends(get_db)):
    token = auth.login(db=db, user=user)
    if "error" in token:
        return response_data(status.HTTP_401_UNAUTHORIZED, "Login failed!", datetime.now(), token)
    return response_data(status.HTTP_200_OK, "Login successful!", datetime.now(), {"access_token": token})

@router.post("/get_user")
def get_current_user(token:str = Header(), db:Session = Depends(get_db)):
    user = auth.get_current_user(db, token)
    
    if "InvalidToken" in user or "ExpiredToken" in user:
        return response_data(status.HTTP_401_UNAUTHORIZED, "Unauthorized!", datetime.now(), user)
    
    if "UserNotFound" in user:
        return response_data(status.HTTP_404_NOT_FOUND, "User not found!", datetime.now(), user)
    
    return response_data(status.HTTP_200_OK, "Successful!", datetime.now(), user)
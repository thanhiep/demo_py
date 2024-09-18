from fastapi import APIRouter, Depends, status, Body
from sqlalchemy.orm import Session
from ..schemas import UserSignUp
from ..database import get_db
from ..crud import auth
from ..config.response import response_data
from datetime import datetime

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup", status_code=status.HTTP_201_CREATED)
def sign_up(user: UserSignUp = Body(), db: Session = Depends(get_db)):
    new_user = auth.sign_up(db=db,user=user)
    if new_user is None:
        return response_data(status.HTTP_409_CONFLICT,"Email already exists!",datetime.now(),"")
    return response_data(status.HTTP_201_CREATED,"Sign up successful!", datetime.now(),"")
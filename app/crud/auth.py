from sqlalchemy.orm import Session
from sqlalchemy import update
from ..schemas import UserSignUp, UserLogin, UserWithId
from ..models import NguoiDung
from passlib.context import CryptContext
from ..config.jwt import create_token, create_token_ref, decode_token
import time

pw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pw_context.hash(password)


def verify_password(plain_password: str, hash_password: str) -> bool:
    return pw_context.verify(plain_password, hash_password)


def check_exist_user(db: Session, email: str):
    db_user = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if db_user:
        return True
    return False


def sign_up(db: Session, user: UserSignUp):
    exist_user = check_exist_user(db, user.email)
    if exist_user:
        return None

    db_user = NguoiDung(
        email=user.email,
        mat_khau=hash_password(user.mat_khau),
        ho_ten=user.ho_ten,
        tuoi=user.tuoi,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def login(db: Session, user: UserLogin):
    db_user_email = db.query(NguoiDung).filter(NguoiDung.email == user.email).first()
    if db_user_email:
        if verify_password(user.mat_khau, db_user_email.mat_khau):
            key = time.time()
            token = create_token(
                {
                    "userID": db_user_email.nguoi_dung_id,
                    "email": db_user_email.email,
                    "key": key,
                }
            )
            token_ref = create_token_ref(
                {
                    "userID": db_user_email.nguoi_dung_id,
                    "email": db_user_email.email,
                    "key": key,
                }
            )
            db_user_email.refresh_token = token_ref
            db.commit()
        else:
            token = {"error": "Wrong password!"}
    else:
        token = {"error": "Wrong email!"}
    return token

def get_current_user(db:Session, token:str):
    data_decode = decode_token(token)
    if "data" in data_decode and "userID" in data_decode["data"]:
        user = db.query(NguoiDung).filter(NguoiDung.nguoi_dung_id == data_decode["data"]["userID"]).first()
        if not user:
            return {"UserNotFound": "User does not exist"}
        return UserWithId.model_validate(user)
    return data_decode
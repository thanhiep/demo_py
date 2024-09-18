from sqlalchemy.orm import Session
from ..schemas import UserSignUp
from ..models import NguoiDung
from passlib.context import CryptContext

pw_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password:str) -> str:
    return pw_context.hash(password)

def verify_password(plain_password: str, hash_password: str) -> bool:
    return pw_context.verify(plain_password, hash_password)

def check_user(db:Session, email: str):
    db_user = db.query(NguoiDung).filter(NguoiDung.email == email).first()
    if db_user:
        return True
    return False

def sign_up(db:Session, user: UserSignUp):
    exist_user = check_user(db,user.email)
    if exist_user:
        return None
    
    db_user = NguoiDung(
        email = user.email,
        mat_khau = hash_password(user.mat_khau),
        ho_ten = user.ho_ten,
        tuoi = user.tuoi
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
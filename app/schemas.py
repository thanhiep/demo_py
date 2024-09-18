from pydantic import BaseModel, EmailStr

class Image(BaseModel):
    hinh_id: int
    ten_hinh: str
    duong_dan: str
    mo_ta: str
    nguoi_dung: "UserWithId"
    
    class Config:
        orm_mode = True
        from_attributes=True
    
class CreateImage(Image):
    pass 
    
class User(BaseModel):
    email: str
    ho_ten: str
    tuoi: int
    anh_dai_dien: str
    
    class Config:
        orm_mode = True
        from_attributes=True
    
class CreateUser(User):
    pass

class UserWithId(User):
    nguoi_dung_id: int    
    
class UserLogin(BaseModel):
    email: EmailStr
    mat_khau: str
    
class UserSignUp(BaseModel):
    email: EmailStr
    mat_khau: str
    ho_ten: str
    tuoi: int
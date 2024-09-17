from pydantic import BaseModel

class Image(BaseModel):
    ten_hinh: str
    duong_dan: str
    mo_ta: str
    nguoi_dung_id: int
    
class CreateImage(Image):
    pass 
    
class ImageWithId(Image):
    hinh_id: int
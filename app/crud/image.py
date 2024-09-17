from sqlalchemy.orm import Session
from .. import models, schemas

def read_image(db: Session) -> list[schemas.ImageWithId]:
    img = db.query(models.HinhAnh).all()
    return img
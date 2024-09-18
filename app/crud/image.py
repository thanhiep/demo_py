from sqlalchemy.orm import Session, joinedload
from .. import schemas
from ..models import HinhAnh, NguoiDung


def read_image(db: Session) -> list[schemas.Image]:
    img = db.query(HinhAnh).options(joinedload(HinhAnh.nguoi_dung)).all()
    return [schemas.Image.model_validate(image) for image in img]


def get_image_by_id(db: Session, id: int) -> schemas.Image:
    img = (
        db.query(HinhAnh)
        .filter(HinhAnh.hinh_id == id)
        .options(joinedload(HinhAnh.nguoi_dung))
        .first()
    )

    if img is None:
        return None

    return schemas.Image.model_validate(img)

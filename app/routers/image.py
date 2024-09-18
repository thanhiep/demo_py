from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from ..database import get_db
from ..crud import image
from sqlalchemy.orm import Session
from ..config.response import response_data
from datetime import datetime

router = APIRouter(prefix="/img", tags=["Image"])


@router.get("/", response_class=JSONResponse)
async def read_img(db: Session = Depends(get_db)):
    data = image.read_image(db)
    return response_data(status.HTTP_200_OK, "Successful", datetime.now(), data)


@router.get("/{id}", response_class=JSONResponse)
async def get_img_by_id(id: int, db: Session = Depends(get_db)):
    data = image.get_image_by_id(db, id)

    if data is None:
        return response_data(
            status.HTTP_404_NOT_FOUND, "The image doesn't exist", datetime.now(), ""
        )

    return response_data(status.HTTP_200_OK, "Successful", datetime.now(), data)

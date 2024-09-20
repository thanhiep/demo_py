from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from ..database import get_db
from ..crud import image
from sqlalchemy.orm import Session
from ..config.response import response_data
from datetime import datetime
from ..config.jwt_bearer import jwtBearer

router = APIRouter(prefix="/img", tags=["Image"])


@router.get("/", dependencies=[Depends(jwtBearer())] ,response_class=JSONResponse)
def read_img(db: Session = Depends(get_db)):
    try:
        data = image.read_image(db)
        return response_data(status.HTTP_200_OK, "Successful", datetime.now(), data)
    except Exception as e:
         return response_data(status.HTTP_500_INTERNAL_SERVER_ERROR, f"An error occurred: {str(e)}", datetime.now(), "data")


@router.get("/{id}", response_class=JSONResponse)
def get_img_by_id(id: int, db: Session = Depends(get_db)):
    data = image.get_image_by_id(db, id)

    if data is None:
        return response_data(
            status.HTTP_404_NOT_FOUND, "The image doesn't exist", datetime.now(), ""
        )

    return response_data(status.HTTP_200_OK, "Successful", datetime.now(), data)

from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models, auth
from sqlalchemy.orm import Session
from repository import mkdetail

router = APIRouter(
    prefix = "/mkdetail",
    tags = ['Matakuliah Detail']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowMkdetail], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return mkdetail.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Mkdetail, db: Session = Depends(get_db)):
    return mkdetail.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return mkdetail.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Mkdetail, db: Session = Depends(get_db)):
    return mkdetail.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowMkdetail)
def show(id: int, db: Session = Depends(get_db)):
    return mkdetail.show(id, db)

from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models
from sqlalchemy.orm import Session
from repository import matakuliah

router = APIRouter(
    prefix = "/matakuliah",
    tags = ['Matakuliah']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowMatakuliah], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return matakuliah.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Matakuliah, db: Session = Depends(get_db)):
    return matakuliah.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return matakuliah.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Matakuliah, db: Session = Depends(get_db)):
    return matakuliah.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowMatakuliah)
def show(id: int, db: Session = Depends(get_db)):
    return matakuliah.show(id, db)

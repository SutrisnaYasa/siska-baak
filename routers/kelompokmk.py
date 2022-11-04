from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models
from sqlalchemy.orm import Session
from repository import kelompokmk

router = APIRouter(
    prefix = "/kelompokmk",
    tags = ['Kelompok Matakuliah']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowKelompokmk], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return kelompokmk.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Kelompokmk, db: Session = Depends(get_db)):
    return kelompokmk.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return kelompokmk.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Kelompokmk, db: Session = Depends(get_db)):
    return kelompokmk.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowKelompokmk)
def show(id: int, db: Session = Depends(get_db)):
    return kelompokmk.show(id, db)

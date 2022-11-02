from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models
from sqlalchemy.orm import Session
from repository import kelas

router = APIRouter(
    prefix = "/kelas",
    tags = ['Kelas']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowKelas], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return kelas.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Kelas, db: Session = Depends(get_db)):
    return kelas.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return kelas.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Kelas, db: Session = Depends(get_db)):
    return kelas.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowKelas)
def show(id: int, db: Session = Depends(get_db)):
    return kelas.show(id, db)


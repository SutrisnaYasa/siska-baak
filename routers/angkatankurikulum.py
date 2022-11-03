from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models
from sqlalchemy.orm import Session
from repository import angkatankurikulum

router = APIRouter(
    prefix = "/angkatankurikulum",
    tags = ['Angkatan Kurikulum']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowAngkatanKurikulum], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return angkatankurikulum.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.AngkatanKurikulum, db: Session = Depends(get_db)):
    return angkatankurikulum.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return angkatankurikulum.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.AngkatanKurikulum, db: Session = Depends(get_db)):
    return angkatankurikulum.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowAngkatanKurikulum)
def show(id: int, db: Session = Depends(get_db)):
    return angkatankurikulum.show(id, db)

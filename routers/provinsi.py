from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from repository import provinsi

router = APIRouter(
    prefix = "/provinsi",
    tags = ['Provinsi']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowProvinsi], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return provinsi.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Provinsi, db: Session = Depends(get_db)):
    return provinsi.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return provinsi.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Provinsi, db: Session = Depends(get_db)):
    return provinsi.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowProvinsi)
def show(id: int, db: Session = Depends(get_db)):
    return provinsi.show(id, db)

from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from repository import kabupaten

router = APIRouter(
    prefix = "/kabupaten",
    tags = ['Kabupaten']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowKabupaten], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return kabupaten.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Kabupaten, db: Session = Depends(get_db)):
    return kabupaten.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return kabupaten.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Kabupaten, db: Session = Depends(get_db)):
    return kabupaten.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowKabupaten)
def show(id: int, db: Session = Depends(get_db)):
    return kabupaten.show(id, db)

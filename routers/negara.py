from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from repository import negara

router = APIRouter(
    prefix = "/negara",
    tags = ['Negara']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowNegara], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    return negara.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Negara, db: Session = Depends(get_db)):
    return negara.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return negara.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Negara, db: Session = Depends(get_db)):
    return negara.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowNegara)
def show(id: int, db: Session = Depends(get_db)):
    return negara.show(id, db)

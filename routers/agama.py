from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
import schemas, database, models, auth
from sqlalchemy.orm import Session
from repository import agama

router = APIRouter(
    prefix = "/agama",
    tags = ['Agama']
)
get_db = database.get_db

@router.get('/', response_model = List[schemas.ShowAgama], status_code = status.HTTP_200_OK)
def all(db: Session = Depends(get_db), active: bool = Depends(auth.check_admin)):
    return agama.get_all(db)

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Agama, db: Session = Depends(get_db)):
    return agama.create(request, db)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return agama.destroy(id, db)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Agama, db: Session = Depends(get_db)):
    return agama.update(id, request, db)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowAgama)
def show(id: int, db: Session = Depends(get_db)):
    return agama.show(id, db)

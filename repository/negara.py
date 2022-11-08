from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    negaras = db.query(models.Negara).all()
    return negaras

def create(request: schemas.Negara, db: Session):
    new_negara = models.Negara(nama_negara = request.nama_negara)
    db.add(new_negara)
    db.commit()
    db.refresh(new_negara)
    return new_negara

def destroy(id: int, db: Session):
    negara = db.query(models.Negara).filter(models.Negara.id_negara == id)
    if not negara.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Negara dengan id {id} tidak ditemukan")
    negara.delete(synchronize_session = False)
    db.commit()
    return 'Data Negara Berhasil di Hapus'

def update(id: int, request: schemas.Negara, db: Session):
    negara = db.query(models.Negara).filter(models.Negara.id_negara == id)
    if not negara.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Negara dengan id {id} tidak ditemukan")
    negara.update(request.dict())
    db.commit()
    return 'Data Negara Berhasil di Update'

def show(id: int, db: Session):
    negara = db.query(models.Negara).filter(models.Negara.id_negara == id).first()
    if not negara:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Negara dengan id {id} tidak ditemukan")
    return negara

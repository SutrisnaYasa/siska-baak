from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    gedung_all = db.query(models.Gedung).all()
    return gedung_all

def create(request: schemas.Gedung, db: Session):
    new_gedung = models.Gedung(kd_gedung = request.kd_gedung, nama_gedung = request.nama_gedung)
    db.add(new_gedung)
    db.commit()
    db.refresh(new_gedung)
    return new_gedung

def destroy(id: int, db: Session):
    gedung = db.query(models.Gedung).filter(models.Gedung.id == id)
    if not gedung.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Gedung dengan id {id} tidak ditemukan")
    gedung.delete(synchronize_session = False)
    db.commit()
    return 'Data Gedung Berhasil di Hapus'

def update(id: int, request: schemas.Gedung, db: Session):
    gedung = db.query(models.Gedung).filter(models.Gedung.id == id)
    if not gedung.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Geudng dengan id {id} tidak ditemukan")
    gedung.update(request.dict())
    db.commit()
    return 'Data Gedung Berhasil di Update'

def show(id: int, db: Session):
    gedung = db.query(models.Gedung).filter(models.Gedung.id == id).first()
    if not gedung:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Gedung dengan id {id} tidak ditemukan")
    return gedung

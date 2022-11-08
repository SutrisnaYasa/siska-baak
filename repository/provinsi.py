from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    provinsi_all = db.query(models.Provinsi).all()
    return provinsi_all

def create(request: schemas.Provinsi, db: Session):
    new_provinsi = models.Provinsi(nama_provinsi = request.nama_provinsi)
    db.add(new_provinsi)
    db.commit()
    db.refresh(new_provinsi)
    return new_provinsi

def destroy(id: int, db: Session):
    provinsi = db.query(models.Provinsi).filter(models.Provinsi.id_provinsi == id)
    if not provinsi.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Provinsi dengan id {id} tidak ditemukan")
    provinsi.delete(synchronize_session = False)
    db.commit()
    return 'Data Provinsi Berhasil di Hapus'

def update(id: int, request: schemas.Provinsi, db: Session):
    provinsi = db.query(models.Provinsi).filter(models.Provinsi.id_provinsi == id)
    if not provinsi.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Provinsi dengan id {id} tidak ditemukan")
    provinsi.update(request.dict())
    db.commit()
    return 'Data Provinsi Berhasil di Update'

def show(id: int, db: Session):
    provinsi = db.query(models.Provinsi).filter(models.Provinsi.id_provinsi == id).first()
    if not provinsi:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Provinsi dengan id {id} tidak ditemukan")
    return provinsi

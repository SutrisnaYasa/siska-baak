from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    kecamatans = db.query(models.Kecamatan).all()
    return kecamatans

def create(request: schemas.Kecamatan, db: Session):
    new_kecamatan = models.Kecamatan(nama_kecamatan = request.nama_kecamatan)
    db.add(new_kecamatan)
    db.commit()
    db.refresh(new_kecamatan)
    return new_kecamatan

def destroy(id: int, db: Session):
    kecamatan = db.query(models.Kecamatan).filter(models.Kecamatan.id_kecamatan == id)
    if not kecamatan.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kecamatan dengan id {id} tidak ditemukan")
    kecamatan.delete(synchronize_session = False)
    db.commit()
    return 'Data Kecamatan Berhasil di Hapus'

def update(id: int, request: schemas.Kecamatan, db: Session):
    kecamatan = db.query(models.Kecamatan).filter(models.Kecamatan.id_kecamatan == id)
    if not kecamatan.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kecamatan dengan id {id} tidak ditemukan")
    kecamatan.update(request.dict())
    db.commit()
    return 'Data Kecamatan Berhasil di Update'

def show(id: int, db: Session):
    kecamatan = db.query(models.Kecamatan).filter(models.Kecamatan.id_kecamatan == id).first()
    if not kecamatan:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kecamatan dengan id {id} tidak ditemukan")
    return kecamatan
        
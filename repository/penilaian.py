from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    penilaian_all = db.query(models.Penilaian).all()
    return penilaian_all

def create(request: schemas.Penilaian, db: Session):
    new_penilaian = models.Penilaian(nama_nilai = request.nama_nilai, per_min = request.per_min, per_max = request.per_max, status_penilaian = request.status_penilaian)
    db.add(new_penilaian)
    db.commit()
    db.refresh(new_penilaian)
    return new_penilaian

def destroy(id: int, db: Session):
    penilaian = db.query(models.Penilaian).filter(models.Penilaian.id_nilai == id)
    if not penilaian.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Penilaian dengan id {id} tidak ditemukan")
    penilaian.delete(synchronize_session = False)
    db.commit()
    return 'Data Penilaian Berhasil di Hapus'

def update(id: int, request: schemas.Penilaian, db: Session):
    penilaian = db.query(models.Penilaian).filter(models.Penilaian.id_nilai == id)
    if not penilaian.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Penilaian dengan id {id} tidak ditemukan")
    penilaian.update(request.dict())
    db.commit()
    return 'Data Penilaian Berhasil di Update'

def show(id: int, db: Session):
    penilaian = db.query(models.Penilaian).filter(models.Penilaian.id_nilai == id).first()
    if not penilaian:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Penilaian dengan id {id} tidak ditemukan")
    return penilaian

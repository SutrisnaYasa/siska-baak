from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    kelas_all = db.query(models.Kelas).all()
    return kelas_all

def create(request: schemas.Kelas, db: Session):
    new_kelas = models.Kelas(kd_kelas = request.kd_kelas, nama_kelas = request.nama_kelas)
    db.add(new_kelas)
    db.commit()
    db.refresh(new_kelas)
    return new_kelas

def destroy(id: int, db: Session):
    kelas = db.query(models.Kelas).filter(models.Kelas.id == id)
    if not kelas.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kelas dengan id {id} tidak ditemukan")
    kelas.delete(synchronize_session = False)
    db.commit()
    return 'Data Kelas Berhasil di Hapus'

def update(id: int, request: schemas.Kelas, db: Session):
    kelas = db.query(models.Kelas).filter(models.Kelas.id == id)
    if not kelas.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kelas dengan id {id} tidak ditemukan")
    kelas.update(request.dict())
    db.commit()
    return 'Data Kelas Berhasil di Update'

def show(id: int, db: Session):
    kelas = db.query(models.Kelas).filter(models.Kelas.id == id).first()
    if not kelas:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kelas dengan id {id} tidak ditemukan")
    return kelas


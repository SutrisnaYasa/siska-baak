from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    ruangan_all = db.query(models.Ruangan).all()
    return ruangan_all

def create(request: schemas.Ruangan, db: Session):
    new_ruangan = models.Ruangan(kd_ruangan = request.kd_ruangan, nama_ruangan = request.nama_ruangan, jml_kapasitas = request.jml_kapasitas, id_gedung = request.id_gedung )
    db.add(new_ruangan)
    db.commit()
    db.refresh(new_ruangan)
    return new_ruangan

def destroy(id: int, db: Session):
    ruangan = db.query(models.Ruangan).filter(models.Ruangan.id == id)
    if not ruangan.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Ruangan dengan id {id} tidak ditemukan")
    ruangan.delete(synchronize_session = False)
    db.commit()
    return 'Data Ruangan Berhasil di Hapus'

def update(id: int, request: schemas.Ruangan, db: Session):
    ruangan = db.query(models.Ruangan).filter(models.Ruangan.id == id)
    if not ruangan.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Ruangan dengan id {id} tidak ditemukan")
    ruangan.update(request.dict())
    db.commit()
    return 'Data Ruangan Berhasil di Update'

def show(id: int, db: Session):
    ruangan = db.query(models.Ruangan).filter(models.Ruangan.id == id).first()
    if not ruangan:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Ruangan dengan id {id} tidak ditemukan")
    return ruangan

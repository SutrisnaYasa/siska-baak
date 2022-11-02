from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    agamas = db.query(models.Agama).all()
    return agamas

def create(request: schemas.Agama, db: Session):
    new_agama = models.Agama(kd_agama = request.kd_agama, nama_agama = request.nama_agama)
    db.add(new_agama)
    db.commit()
    db.refresh(new_agama)
    return new_agama

def destroy(id: int, db: Session):
    agama = db.query(models.Agama).filter(models.Agama.id == id)
    if not agama.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Agama dengan id {id} tidak ditemukan")
    agama.delete(synchronize_session = False)
    db.commit()
    return 'Data Agama Berhasil di Hapus'

def update(id: int, request: schemas.Agama, db: Session):
    agama = db.query(models.Agama).filter(models.Agama.id == id)
    if not agama.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Agama dengan id {id} tidak ditemukan")
    agama.update(request.dict())
    db.commit()
    return 'Data Agama Berhasil di Update'

def show(id: int, db: Session):
    agama = db.query(models.Agama).filter(models.Agama.id == id).first()
    if not agama:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Agama dengan id {id} tidak ditemukan")
    return agama

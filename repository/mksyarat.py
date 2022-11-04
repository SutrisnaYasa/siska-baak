from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    mksyarats = db.query(models.Mksyarat).all()
    return mksyarats

def create(request: schemas.Mksyarat, db: Session):
    new_mksyarat = models.Mksyarat(kode_mk = request.kode_mk, kd_mk_syarat_and = request.kd_mk_syarat_and, kd_mk_syarat_or = request.kd_mk_syarat_or)
    db.add(new_mksyarat)
    db.commit()
    db.refresh(new_mksyarat)
    return new_mksyarat

def destroy(id: int, db: Session):
    mksyarat = db.query(models.Mksyarat).filter(models.Mksyarat.id_mk_syarat == id)
    if not mksyarat.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah Syarat dengan id {id} tidak ditemukan")
    mksyarat.delete(synchronize_session = False)
    db.commit()
    return 'Data Matakuliah Syarat Berhasil di Hapus'

def update(id: int, request: schemas.Mksyarat, db: Session):
    mksyarat = db.query(models.Mksyarat).filter(models.Mksyarat.id_mk_syarat == id)
    if not mksyarat.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah Syarat dengan id {id} tidak ditemukan")
    mksyarat.update(request.dict())
    db.commit()
    return 'Data Matakuliah Syarat Berhasil di Update'

def show(id: int, db: Session):
    mksyarat = db.query(models.Mksyarat).filter(models.Mksyarat.id_mk_syarat == id).first()
    if not mksyarat:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah Syarat dengan id {id} tidak ditemukan")
    return mksyarat

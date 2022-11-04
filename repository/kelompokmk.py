from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    kelompokmks = db.query(models.Kelompokmk).all()
    return kelompokmks

def create(request: schemas.Kelompokmk, db: Session):
    new_kelompokmk = models.Kelompokmk(kode_klp = request.kode_klp, nm_klp_mk = request.nm_klp_mk, koordinator = request.koordinator, matkul = request.matkul)
    db.add(new_kelompokmk)
    db.commit()
    db.refresh(new_kelompokmk)
    return new_kelompokmk

def destroy(id: int, db: Session):
    kelompokmk = db.query(models.Kelompokmk).filter(models.Kelompokmk.id_klp_mk == id)
    if not kelompokmk.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kelompok Matakuliah dengan id {id} tidak ditemukan")
    kelompokmk.delete(synchronize_session = False)
    db.commit()
    return 'Data Kelompok Matakuliah Berhasil di Hapus'

def update(id: int, request: schemas.Kelompokmk, db: Session):
    kelompokmk = db.query(models.Kelompokmk).filter(models.Kelompokmk.id_klp_mk == id)
    if not kelompokmk.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kelompok Matakuliah dengan id {id} tidak ditemukan")
    kelompokmk.update(request.dict())
    db.commit()
    return 'Data Kelompok Matakuliah Berhasil Update'

def show(id: int, db: Session):
    kelompokmk = db.query(models.Kelompokmk).filter(models.Kelompokmk.id_klp_mk == id).first()
    if not kelompokmk:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kelompok Matakuliah dengan id {id} tidak ditemukan")
    return kelompokmk

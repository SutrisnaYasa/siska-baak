from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    mkkelas_all = db.query(models.Mkkelas).all()
    return mkkelas_all

def create(request: schemas.Mkkelas, db: Session):
    new_mkkelas = models.Mkkelas(kode_kelas_mk = request.kode_kelas_mk, nm_kelas_mk = request.nm_kelas_mk)
    db.add(new_mkkelas)
    db.commit()
    db.refresh(new_mkkelas)
    return new_mkkelas

def destroy(id: int, db: Session):
    mkkelas = db.query(models.Mkkelas).filter(models.Mkkelas.id_mk_kelas == id)
    if not mkkelas.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah Kelas dengan id {id} tidak ditemukan")
    mkkelas.delete(synchronize_session = False)
    db.commit()
    return 'Data Matakuliah Kelas Berhasil di Hapus'

def update(id: int, request: schemas.Mkkelas, db: Session):
    mkkelas = db.query(models.Mkkelas).filter(models.Mkkelas.id_mk_kelas == id)
    if not mkkelas.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah Kelas dengan id {id} tidak ditemukan")
    mkkelas.update(request.dict())
    db.commit()
    return 'Data Matakuliah Kelas Berhasil di Update'

def show(id: int, db: Session):
    mkkelas = db.query(models.Mkkelas).filter(models.Mkkelas.id_mk_kelas == id).first()
    if not mkkelas:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah Kelas dengan id {id} tidak ditemukan")
    return mkkelas

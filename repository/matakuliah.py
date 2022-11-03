from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    matakuliah_all = db.query(models.Matakuliah).all()
    return matakuliah_all

def create(request: schemas.Matakuliah, db: Session):
    new_matakuliah = models.Matakuliah(kode_mk = request.kode_mk, nama_makul = request.nama_makul, deskripsi = request.deskripsi)
    db.add(new_matakuliah)
    db.commit()
    db.refresh(new_matakuliah)
    return new_matakuliah

def destroy(id: int, db: Session):
    matakuliah = db.query(models.Matakuliah).filter(models.Matakuliah.id_makul == id)
    if not matakuliah.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah dengan id {id} tidak ditemukan")
    matakuliah.delete(synchronize_session = False)
    db.commit()
    return 'Data Matakuliah Berhasil di Hapus'

def update(id: int, request: schemas.Matakuliah, db: Session):
    matakuliah = db.query(models.Matakuliah).filter(models.Matakuliah.id_makul == id)
    if not matakuliah.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah dengan id {id} tidak ditemukan")
    matakuliah.update(request.dict())
    db.commit()
    return 'Data Matakuliah Berhasil di Update'

def show(id: int, db: Session):
    matakuliah = db.query(models.Matakuliah).filter(models.Matakuliah.id_makul == id).first()
    if not matakuliah:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah dengan id {id} tidak ditemukan")
    return matakuliah

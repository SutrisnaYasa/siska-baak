from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    mkdetail_all = db.query(models.Mkdetail).all()
    return mkdetail_all

def create(request: schemas.Mkdetail, db: Session):
    new_mkdetail = models.Mkdetail(kode_mk = request.kode_mk, course = request.course, klp_mk = request.klp_mk, prodi = request.prodi, sks = request.sks, semester = request.semester, thn_kurikulum = request.thn_kurikulum)
    db.add(new_mkdetail)
    db.commit()
    db.refresh(new_mkdetail)
    return new_mkdetail

def destroy(id: int, db: Session):
    mkdetail = db.query(models.Mkdetail).filter(models.Mkdetail.id_mk_detail == id)
    if not mkdetail.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah Detail dengan id {id} tidak ditemukan")
    mkdetail.delete(synchronize_session = False)
    db.commit()
    return 'Data Matakuliah Detail Berhasil di Hapus'

def update(id: int, request: schemas.Mkdetail, db: Session):
    mkdetail = db.query(models.Mkdetail).filter(models.Mkdetail.id_mk_detail == id)
    if not mkdetail.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah Detail dengan id {id} tidak ditemukan")
    mkdetail.update(request.dict())
    db.commit()
    return 'Data Matakuliah Detail Berhasil di Update'

def show(id: int, db: Session):
    mkdetail = db.query(models.Mkdetail).filter(models.Mkdetail.id_mk_detail == id).first()
    if not mkdetail:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Matakuliah Detail dengan id {id} tidak ditemukan")
    return mkdetail

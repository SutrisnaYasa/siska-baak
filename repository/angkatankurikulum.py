from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    angkatankurikulum_all = db.query(models.AngkatanKurikulum).all()
    return angkatankurikulum_all

def create(request: schemas.AngkatanKurikulum, db: Session):
    new_angkatan_kurikulum = models.AngkatanKurikulum(angkatan_krk = request.angkatan_krk, kurikulumThn = request.kurikulumThn)
    db.add(new_angkatan_kurikulum)
    db.commit()
    db.refresh(new_angkatan_kurikulum)
    return new_angkatan_kurikulum

def destroy(id: int, db: Session):
    angkatankurikulum = db.query(models.AngkatanKurikulum).filter(models.AngkatanKurikulum.id_angkatan_krk == id)
    if not angkatankurikulum.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Angkatan Kurikulum dengan id {id} tidak ditemukan")
    angkatankurikulum.delete(synchronize_session = False)
    db.commit()
    return 'Data Angkatan Kurikulum Berhasil di Hapus'


def update(id: int, request: schemas.AngkatanKurikulum, db: Session):
    angkatankurikulum = db.query(models.AngkatanKurikulum).filter(models.AngkatanKurikulum.id_angkatan_krk == id)
    if not angkatankurikulum.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Angkatan Kurikulum dengan id {id} tidak ditemukan")
    angkatankurikulum.update(request.dict())
    db.commit()
    return 'Data Angkatan Kurikulum Berhasil di Update'

def show(id: int, db: Session):
    angkatankurikulum = db.query(models.AngkatanKurikulum).filter(models.AngkatanKurikulum.id_angkatan_krk == id).first()
    if not angkatankurikulum:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Angkatan Kurikulum dengan id {id} tidak ditemukan")
    return angkatankurikulum

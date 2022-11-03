from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    kurikulum_all = db.query(models.Kurikulum).all()
    return kurikulum_all

def create(request: schemas.Kurikulum, db: Session):
    new_kurikulum = models.Kurikulum(thn_kurikulum = request.thn_kurikulum, stts_kurikulum = request.stts_kurikulum, keterangan = request.keterangan)
    db.add(new_kurikulum)
    db.commit()
    db.refresh(new_kurikulum)
    return new_kurikulum

def destroy(id: int, db: Session):
    kurikulum = db.query(models.Kurikulum).filter(models.Kurikulum.id_kurikulum == id)
    if not kurikulum.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kurikulum dengan id {id} tidak ditemukan")
    kurikulum.delete(synchronize_session = False)
    db.commit()
    return 'Data Kurikulum Berhasil di Hapus'

def update(id: int, request: schemas.Kurikulum, db: Session):
    kurikulum = db.query(models.Kurikulum).filter(models.Kurikulum.id_kurikulum == id)
    if not kurikulum.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kurikulum dengan id {id} tidak ditemukan")
    kurikulum.update(request.dict())
    db.commit()
    return 'Data Kurikulum Berhasil di Update'

def show(id: int, db: Session):
    kurikulum = db.query(models.Kurikulum).filter(models.Kurikulum.id_kurikulum == id).first()
    if not kurikulum:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kurikulum dengan id {id} tidak ditemukan")
    return kurikulum

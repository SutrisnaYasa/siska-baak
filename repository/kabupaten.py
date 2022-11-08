from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    kabupatens = db.query(models.Kabupaten).all()
    return kabupatens

def create(request: schemas.Kabupaten, db: Session):
    new_kabupaten = models.Kabupaten(nama_kabupaten = request.nama_kabupaten)
    db.add(new_kabupaten)
    db.commit()
    db.refresh(new_kabupaten)
    return new_kabupaten

def destroy(id: int, db: Session):
    kabupaten = db.query(models.Kabupaten).filter(models.Kabupaten.id_kabupaten == id)
    if not kabupaten.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kabupaten dengan id {id} tidak ditemukan")
    kabupaten.delete(synchronize_session = False)
    db.commit()
    return 'Data Kabupaten Berhasil di Hapus'

def update(id: int, request: schemas.Kabupaten, db: Session):
    kabupaten = db.query(models.Kabupaten).filter(models.Kabupaten.id_kabupaten == id)
    if not kabupaten.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kabupaten dengan id {id} tidak ditemukan")
    kabupaten.update(request.dict())
    db.commit()
    return 'Data Kabupaten Berhasil di Update'

def show(id: int, db: Session):
    kabupaten = db.query(models.Kabupaten).filter(models.Kabupaten.id_kabupaten == id).first()
    if not kabupaten:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Kabupaten dengan id {id} tidak ditemukan")
    return kabupaten

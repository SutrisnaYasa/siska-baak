from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    grades = db.query(models.Grade).all()
    return grades

def create(request: schemas.Grade, db: Session):
    new_grade = models.Grade(batas_bawah = request.batas_bawah, batas_atas = request.batas_atas, nilai_huruf = request.nilai_huruf, bobot = request.bobot)
    db.add(new_grade)
    db.commit()
    db.refresh(new_grade)
    return new_grade

def destroy(id: int, db: Session):
    grade = db.query(models.Grade).filter(models.Grade.id_grade == id)
    if not grade.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Grade dengan id {id} tidak ditemukan")
    grade.delete(synchronize_session = False)
    db.commit()
    return 'Data Grade Berhasil di Hapus'

def update(id: int, request: schemas.Grade, db: Session):
    grade = db.query(models.Grade).filter(models.Grade.id_grade == id)
    if not grade.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Grade dengan id {id} tidak ditemukan")
    grade.update(request.dict())
    db.commit()
    return 'Data Grade Berhasil di Update'

def show(id: int, db: Session):
    grade = db.query(models.Grade).filter(models.Grade.id_grade == id).first()
    if not grade:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Grade dengan id {id} tidak ditemukan")
    return grade

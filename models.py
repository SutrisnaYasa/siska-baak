from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

# Models untuk Master Agama
class Agama(Base):
    __tablename__ = 'master_agama'
    id = Column(Integer, primary_key = True, index = True)
    kd_agama = Column(String(10))
    nama_agama = Column(String(100))

# Models untuk Master Kelas
class Kelas(Base):
    __tablename__ = 'master_kelas'
    id = Column(Integer, primary_key = True, index = True)
    kd_kelas = Column(String(10))
    nama_kelas = Column(String(100))

# Models untuk Master Gedung
class Gedung(Base):
    __tablename__ = 'master_gedung'
    id = Column(Integer, primary_key = True, index = True)
    kd_gedung = Column(String(10))
    nama_gedung = Column(String(100))
    gedungs = relationship("Ruangan", back_populates = "ruangans")

# Models untuk Master Ruangan
class Ruangan(Base):
    __tablename__ = 'master_ruangan'
    id = Column(Integer, primary_key = True, index = True)
    kd_ruangan = Column(String(10))
    nama_ruangan = Column(String(100))
    jml_kapasitas = Column(Integer)
    id_gedung = Column(Integer, ForeignKey('master_gedung.id'))
    ruangans = relationship("Gedung", back_populates = "gedungs")

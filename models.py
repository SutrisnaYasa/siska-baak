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



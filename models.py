from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Agama(Base):
    __tablename__ = 'master_agama'
    id = Column(Integer, primary_key = True, index = True)
    kd_agama = Column(String(10))
    nama_agama = Column(String(100))

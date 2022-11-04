from sqlalchemy import Column, Integer, String, ForeignKey, Float
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

# Models untuk Master Penilaian
class Penilaian(Base):
    __tablename__ = 'master_penilaian'
    id_nilai = Column(Integer, primary_key = True, index = True)
    nama_nilai = Column(String(100))
    per_min = Column(Integer)
    per_max = Column(Integer)
    status_penilaian = Column(String(100))

# Models untuk Master Grade
class Grade(Base):
    __tablename__ = 'master_grade'
    id_grade = Column(Integer, primary_key = True, index = True)
    batas_bawah = Column(Float)
    batas_atas = Column(Float)
    nilai_huruf = Column(String(10))
    bobot = Column(Float)

# Models untuk Master Fakultas
class Fakultas(Base):
    __tablename__ = 'master_fakultas'
    id_fakultas = Column(Integer, primary_key = True, index = True)
    nama_fakultas = Column(String(100))
    fakultass = relationship("Prodi", back_populates = "prodis")

# Models untuk Master Prodi
class Prodi(Base):
    __tablename__ = 'master_prodi'
    id_prodi = Column(Integer, primary_key = True, index = True)
    kode_prodi = Column(String(10))
    nama_prodi = Column(String(100))
    fakultasID = Column(Integer, ForeignKey('master_fakultas.id_fakultas'))
    prodis = relationship("Fakultas", back_populates = "fakultass")

# Models untuk Master Tahun Kurikulum
class Kurikulum(Base):
    __tablename__ = 'master_kurikulum'
    id_kurikulum = Column(Integer, primary_key = True, index = True)
    thn_kurikulum  = Column(String(50))
    stts_kurikulum = Column(String(50))
    keterangan = Column(String(100))
    kurikulums = relationship("AngkatanKurikulum", back_populates = "angkatankrkm")

# Models untuk Master Angkatan Kurikulum
class AngkatanKurikulum(Base):
    __tablename__ = 'master_angkatan_kurikulum'
    id_angkatan_krk = Column(Integer, primary_key = True, index = True)
    angkatan_krk = Column(String(20))
    kurikulumThn = Column(Integer, ForeignKey('master_kurikulum.id_kurikulum'))
    angkatankrkm = relationship("Kurikulum", back_populates = "kurikulums") 

# Models untuk Master Matakuliah
class Matakuliah(Base):
    __tablename__ = 'master_matakuliah'
    id_makul = Column(Integer, primary_key = True, index = True)
    kode_mk = Column(String(10))
    nama_makul = Column(String(100))
    deskripsi = Column(String(100))

# Models untuk Master Matakuliah Kelas
class Mkkelas(Base):
    __tablename__ = 'master_mkkelas'
    id_mk_kelas = Column(Integer, primary_key = True, index = True)
    kode_kelas_mk = Column(String(10))
    nm_kelas_mk = Column(String(100))

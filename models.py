from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean, Enum
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

# Models Untuk Users
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(100))
    password = Column(String(100))
    is_active = Column(Boolean, default = True)
    role = Column(String(100), nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models untuk Master Agama
class Agama(Base):
    __tablename__ = 'master_agama'
    id = Column(Integer, primary_key = True, index = True)
    kd_agama = Column(String(10))
    nama_agama = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models untuk Master Kelas
class Kelas(Base):
    __tablename__ = 'master_kelas'
    id = Column(Integer, primary_key = True, index = True)
    kd_kelas = Column(String(10))
    nama_kelas = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models untuk Master Gedung
class Gedung(Base):
    __tablename__ = 'master_gedung'
    id = Column(Integer, primary_key = True, index = True)
    kd_gedung = Column(String(10))
    nama_gedung = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    gedungs = relationship("Ruangan", back_populates = "ruangans")

# Models untuk Master Ruangan
class Ruangan(Base):
    __tablename__ = 'master_ruangan'
    id = Column(Integer, primary_key = True, index = True)
    kd_ruangan = Column(String(10))
    nama_ruangan = Column(String(100))
    jml_kapasitas = Column(Integer)
    id_gedung = Column(Integer, ForeignKey('master_gedung.id'))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    ruangans = relationship("Gedung", back_populates = "gedungs")

# Models untuk Master Penilaian
class Penilaian(Base):
    __tablename__ = 'master_penilaian'
    id_nilai = Column(Integer, primary_key = True, index = True)
    nama_nilai = Column(String(100))
    per_min = Column(Integer)
    per_max = Column(Integer)
    status_penilaian = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models untuk Master Grade
class Grade(Base):
    __tablename__ = 'master_grade'
    id_grade = Column(Integer, primary_key = True, index = True)
    batas_bawah = Column(Float)
    batas_atas = Column(Float)
    nilai_huruf = Column(String(10))
    bobot = Column(Float)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models untuk Master Fakultas
class Fakultas(Base):
    __tablename__ = 'master_fakultas'
    id_fakultas = Column(Integer, primary_key = True, index = True)
    nama_fakultas = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    fakultass = relationship("Prodi", back_populates = "prodis")

# Models untuk Master Prodi
class Prodi(Base):
    __tablename__ = 'master_prodi'
    id_prodi = Column(Integer, primary_key = True, index = True)
    kode_prodi = Column(String(10))
    nama_prodi = Column(String(100))
    fakultasID = Column(Integer, ForeignKey('master_fakultas.id_fakultas'))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    prodis = relationship("Fakultas", back_populates = "fakultass")
    mkd_prodis = relationship("Mkdetail", back_populates = "mkd_prodi")

# Models untuk Master Tahun Kurikulum
class Kurikulum(Base):
    __tablename__ = 'master_kurikulum'
    id_kurikulum = Column(Integer, primary_key = True, index = True)
    thn_kurikulum  = Column(String(50))
    stts_kurikulum = Column(String(50))
    keterangan = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    kurikulums = relationship("AngkatanKurikulum", back_populates = "angkatankrkm")
    mkd_thn_kurikulums = relationship("Mkdetail", back_populates = "mkd_thn_kurikulum")

# Models untuk Master Angkatan Kurikulum
class AngkatanKurikulum(Base):
    __tablename__ = 'master_angkatan_kurikulum'
    id_angkatan_krk = Column(Integer, primary_key = True, index = True)
    angkatan_krk = Column(String(20))
    kurikulumThn = Column(Integer, ForeignKey('master_kurikulum.id_kurikulum'))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    angkatankrkm = relationship("Kurikulum", back_populates = "kurikulums")

# Models untuk Master Matakuliah
class Matakuliah(Base):
    __tablename__ = 'master_matakuliah'
    id_makul = Column(Integer, primary_key = True, index = True)
    kode_mk = Column(String(10))
    nama_makul = Column(String(100))
    deskripsi = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    makuls = relationship("Mksyarat", back_populates = "syarats")
    mkd_kode_mks = relationship("Mkdetail", back_populates = "mkd_kode_mk")

# Models untuk Master Matakuliah Kelas
class Mkkelas(Base):
    __tablename__ = 'master_mkkelas'
    id_mk_kelas = Column(Integer, primary_key = True, index = True)
    kode_kelas_mk = Column(String(10))
    nm_kelas_mk = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models untuk Master Matakuliah Syarat
class Mksyarat(Base):
    __tablename__ = 'master_mk_syarat'
    id_mk_syarat = Column(Integer, primary_key = True, index = True)
    kode_mk = Column(Integer, ForeignKey('master_matakuliah.id_makul'))
    kd_mk_syarat_and = Column(String(100))
    kd_mk_syarat_or = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    syarats = relationship("Matakuliah", back_populates = "makuls")

#Models untuk Master Kelompok Matakuliah
class Kelompokmk(Base):
    __tablename__ = 'master_klp_mk'
    id_klp_mk = Column(Integer, primary_key = True, index = True)
    kode_klp = Column(String(100))
    nm_klp_mk = Column(String(100))
    koordinator = Column(String(100))
    matkul = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    mkd_klp_mks = relationship("Mkdetail", back_populates = "mkd_klp_mk")

# Models Untuk Master Matakuliah Detail
class Mkdetail(Base):
    __tablename__ = 'master_mk_detail'
    id_mk_detail= Column(Integer, primary_key = True, index = True)
    kode_mk = Column(Integer, ForeignKey('master_matakuliah.id_makul'))
    course = Column(String(100))
    klp_mk = Column(Integer, ForeignKey('master_klp_mk.id_klp_mk'))
    prodi = Column(Integer, ForeignKey('master_prodi.id_prodi'))
    sks = Column(String(10))
    semester = Column(String(10))
    thn_kurikulum = Column(Integer, ForeignKey('master_kurikulum.id_kurikulum'))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    mkd_kode_mk = relationship("Matakuliah", back_populates = "mkd_kode_mks")
    mkd_klp_mk = relationship("Kelompokmk", back_populates = "mkd_klp_mks")
    mkd_prodi = relationship("Prodi", back_populates = "mkd_prodis")
    mkd_thn_kurikulum = relationship("Kurikulum", back_populates = "mkd_thn_kurikulums")


# Master Daerah
# Models Untuk Master Negara
class Negara(Base):
    __tablename__ = 'master_negara'
    id_negara = Column(Integer, primary_key = True, index = True)
    nama_negara = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models Untuk Master Provinsi
class Provinsi(Base):
    __tablename__ = 'master_provinsi'
    id_provinsi = Column(Integer, primary_key = True, index = True)
    nama_provinsi = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models Untuk Master Kabupaten
class Kabupaten(Base):
    __tablename__ = 'master_kabupaten'
    id_kabupaten = Column(Integer, primary_key = True, index = True)
    nama_kabupaten = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

# Models Untuk Master Kecamatan
class Kecamatan(Base):
    __tablename__ = 'master_kecamatan'
    id_kecamatan = Column(Integer, primary_key = True, index = True)
    nama_kecamatan = Column(String(100))
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())

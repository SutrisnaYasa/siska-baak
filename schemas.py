from typing import List, Optional
from pydantic import BaseModel

# Schemas Untuk Master Agama
class AgamaBase(BaseModel):
    kd_agama: str
    nama_agama: str

class Agama(AgamaBase):
    class Config():
        orm_mode = True

class ShowAgama(BaseModel):
    kd_agama: str
    nama_agama: str

    class Config():
        orm_mode = True
# End Schemas Master Agama

# Schemas Untuk Master Kelas
class KelasBase(BaseModel):
    kd_kelas: str
    nama_kelas: str

class Kelas(KelasBase):
    class Config():
        orm_mode = True

class ShowKelas(BaseModel):
    kd_kelas: str
    nama_kelas: str

    class Config():
        orm_mode = True
# End Schemas Master Kelas

# Schemas Untuk Master Gedung
class GedungBase(BaseModel):
    kd_gedung: str
    nama_gedung: str

class Gedung(GedungBase):
    class Config():
        orm_mode = True

class ShowGedung(BaseModel):
    kd_gedung: str
    nama_gedung: str

    class Config():
        orm_mode = True
# End Schemas Master Gedung

# Schemas Untuk Master Ruangan
class RuanganBase(BaseModel):
    kd_ruangan: str
    nama_ruangan: str
    jml_kapasitas: int
    id_gedung: int

class Ruangan(RuanganBase):
    class Config():
        orm_mode = True

class ShowRuangan(BaseModel):
    kd_ruangan: str
    nama_ruangan: str
    jml_kapasitas: int
    ruangans: ShowGedung

    class Config():
        orm_mode = True
# End Schemas Master Ruangan

# Schemas Untuk Master Penilaian
class PenilaianBase(BaseModel):
    nama_nilai: str
    per_min: int
    per_max: int
    status_penilaian: str

class Penilaian(PenilaianBase):
    class Config():
        orm_mode = True

class ShowPenilaian(BaseModel):
    id_nilai: int
    nama_nilai: str
    per_min: int
    per_max: int
    status_penilaian: str

    class Config():
        orm_mode = True
# End Schemas Master Penilaian

# Schemas Untuk Master Grade
class GradeBase(BaseModel):
    batas_bawah: float
    batas_atas: float
    nilai_huruf: str
    bobot: float

class Grade(GradeBase):
    class Config():
        orm_mode = True

class ShowGrade(BaseModel):
    id_grade: int
    batas_bawah: float
    batas_atas: float
    nilai_huruf: str
    bobot: float

    class Config():
        orm_mode = True

# End Schemas Master Grade

# Schemas Untuk Master Fakultas
class FakultasBase(BaseModel):
    nama_fakultas: str

class Fakultas(FakultasBase):
    class Config():
        orm_mode = True

class ShowFakultas(BaseModel):
    id_fakultas : int
    nama_fakultas: str

    class Config():
        orm_mode = True

# End Schemas Master Fakultas

# Schemas Untuk Master Prodi
class ProdiBase(BaseModel):
    kode_prodi: str
    nama_prodi: str
    fakultasID: int

class Prodi(ProdiBase):
    class Config():
        orm_mode = True

class ShowProdi(BaseModel):
    id_prodi: int
    kode_prodi: str
    nama_prodi: str
    prodis: ShowFakultas

    class Config():
        orm_mode = True

# End Schemas Master Prodi

# Schemas Untuk Master Kurikulum
class KurikulumBase(BaseModel):
    thn_kurikulum: str
    stts_kurikulum: str
    keterangan: str

class Kurikulum(KurikulumBase):
    class Config():
        orm_mode = True

class ShowKurikulum(BaseModel):
    id_kurikulum: int
    thn_kurikulum: str
    stts_kurikulum: str
    keterangan: str

    class Config():
        orm_mode = True

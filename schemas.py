from typing import List, Optional
from pydantic import BaseModel

# Schemas Untuk Users
class User(BaseModel):
    username: str
    password: str

class ShowUser(BaseModel):
    username: str

    class Config():
        orm_mode = True
# End Schemas Untuk User

# Schemas Untuk Login
class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
# End Schemas Untuk Login

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
# End Schemas Master Kurikulum

# Schemas Untuk Master Angkatan Kurikulum
class AngkatanKurikulumBase(BaseModel):
    angkatan_krk: str
    kurikulumThn: int

class AngkatanKurikulum(AngkatanKurikulumBase):
    class Config():
        orm_mode = True

class ShowAngkatanKurikulum(BaseModel):
    id_angkatan_krk: int
    angkatan_krk: str
    angkatankrkm : ShowKurikulum

    class Config():
        orm_mode = True
# End Schemas Master Angkatan Kurikulum

# Schemas Untuk Master Matakuliah
class MatakuliahBase(BaseModel):
    kode_mk: str
    nama_makul: str
    deskripsi: str

class Matakuliah(MatakuliahBase):
    class Config():
        orm_mode = True

class ShowMatakuliah(BaseModel):
    kode_mk: str
    nama_makul: str
    deskripsi: str

    class Config():
        orm_mode = True
# End Schemas Master Matakuliah

# Schemas Untuk Master Matakuliah Kelas
class MkkelasBase(BaseModel):
    kode_kelas_mk: str
    nm_kelas_mk: str

class Mkkelas(MkkelasBase):
    class Config():
        orm_mode = True

class ShowMkkelas(BaseModel):
    kode_kelas_mk: str
    nm_kelas_mk: str

    class Config():
        orm_mode = True
# End Schemas Master Matakuliah Kelas

# Schemas Untuk Master Matakuliah Syarat
class MksyaratBase(BaseModel):
    kode_mk: str
    kd_mk_syarat_and: str
    kd_mk_syarat_or: str

class Mksyarat(MksyaratBase):
    class Config():
        orm_mode = True

class ShowMksyarat(BaseModel):
    syarats: ShowMatakuliah
    kd_mk_syarat_and: str
    kd_mk_syarat_or: str

    class Config():
        orm_mode = True
# End Schemas Master Matakuliah Syarat

# Schemas Untuk Master Kelompok Matakuliah
class KelompokmkBase(BaseModel):
    kode_klp: str
    nm_klp_mk: str
    koordinator: str
    matkul: str

class Kelompokmk(KelompokmkBase):
    class Config():
        orm_mode = True

class ShowKelompokmk(BaseModel):
    kode_klp: str
    nm_klp_mk: str
    koordinator: str
    matkul: str

    class Config():
        orm_mode = True
# End Schemas Master Kelompok Matakuliah

# Schemas Untuk Master Matakuliah Detail
class MkdetailBase(BaseModel):
    kode_mk: int
    course: str
    klp_mk: int
    prodi: int
    sks: str
    semester: str
    thn_kurikulum: int

class Mkdetail(MkdetailBase):
    class Config():
        orm_mode = True

class ShowMkdetail(BaseModel):
    mkd_kode_mk: ShowMatakuliah
    course: str
    mkd_klp_mk: ShowKelompokmk
    mkd_prodi: ShowProdi
    sks: int
    semester: int
    mkd_thn_kurikulum: ShowKurikulum

    class Config():
        orm_mode = True
# End Schemas Untuk Master Matakuliah Detail



# Master Daerah
# Schemas Untuk Master Negara
class NegaraBase(BaseModel):
    nama_negara: str

class Negara(NegaraBase):
    class Config():
        orm_mode = True

class ShowNegara(BaseModel):
    id_negara: int
    nama_negara: str

    class Config():
        orm_mode = True
# End Schemas Master Negara

# Schemas Untuk Master Provinsi
class ProvinsiBase(BaseModel):
    nama_provinsi: str

class Provinsi(ProvinsiBase):
    class Config():
        orm_mode = True

class ShowProvinsi(BaseModel):
    id_provinsi: int
    nama_provinsi: str

    class Config():
        orm_mode = True
# End Schemas Master Provinsi

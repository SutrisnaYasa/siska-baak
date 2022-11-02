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

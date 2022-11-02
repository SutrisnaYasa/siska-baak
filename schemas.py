from typing import List, Optional
from pydantic import BaseModel

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

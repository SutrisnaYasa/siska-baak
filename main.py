from fastapi import FastAPI
import models
from database import engine
from routers import agama, kelas, gedung, ruangan, penilaian, grade, fakultas, prodi, kurikulum, angkatankurikulum, matakuliah, mkkelas

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(agama.router)
app.include_router(kelas.router)
app.include_router(gedung.router)
app.include_router(ruangan.router)
app.include_router(penilaian.router)
app.include_router(grade.router)
app.include_router(fakultas.router)
app.include_router(prodi.router)
app.include_router(kurikulum.router)
app.include_router(angkatankurikulum.router)
app.include_router(matakuliah.router)
app.include_router(mkkelas.router)

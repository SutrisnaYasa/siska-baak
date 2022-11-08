from fastapi import FastAPI
import models
from database import engine
from routers import agama, kelas, gedung, ruangan, penilaian, grade, fakultas, prodi, kurikulum, angkatankurikulum, matakuliah, mkkelas, mksyarat, kelompokmk, user, authentication, mkdetail, negara

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
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
app.include_router(mksyarat.router)
app.include_router(kelompokmk.router)
app.include_router(mkdetail.router)

# Master Daerah
app.include_router(negara.router)

from fastapi import FastAPI
import models
from database import engine
from routers import agama, kelas, gedung

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(agama.router)
app.include_router(kelas.router)
app.include_router(gedung.router)

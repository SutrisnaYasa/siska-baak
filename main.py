from fastapi import FastAPI
import models
from database import engine
from routers import agama

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(agama.router)

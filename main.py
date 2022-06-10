from pkgutil import ImpImporter
from fastapi import Depends, FastAPI
from pydantic import BaseModel, Field
import model
from database import engine
from database import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()
model.Base.metadata.create_all(bind=engine)


@app.get("/")
async def create_db():
    return {"response": "database created"}

from fastapi import FastAPI, Depends 
from sqlalchemy.orm import Session
from models import Base, Todo 
from database import engine, SessionLocal
from typing import Annotated

# FastAPI uygulamasını başlatıyoruz
app = FastAPI()

# Kayıt defterindeki (metadata) tabloları veritabanında fiziksel olarak oluşturur
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/read_all")
async def read_all(db: db_dependency): 
    return db.query(Todo).all()
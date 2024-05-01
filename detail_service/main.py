# Запуск приложения
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

from flask import Flask, request, jsonify

app = Flask(__name__)

class DetailLController:
    def __init__(self):
        # Здесь можно добавить инициализацию необходимых сервисов или объектов

    @app.route('/api/detail_l', methods=['POST'])
    def add_detail_l(self):
        # Здесь будет обработчик для добавления детали

    @app.route('/api/detail_l', methods=['GET'])
    def get_all_detail_ls(self):
        # Здесь будет обработчик для получения всех деталей

    @app.route('/api/detail_l/<int:id>', methods=['GET'])
    def get_detail_l(self, id):
        # Здесь будет обработчик для получения детали по идентификатору

    @app.route('/api/detail_l/<int:id>', methods=['PUT'])
    def update_detail_l(self, id):
        # Здесь будет обработчик для обновления детали

    @app.route('/api/detail_l/<int:id>', methods=['DELETE'])
    def delete_detail_l(self, id):
        # Здесь будет обработчик для удаления детали

    @app.route('/api/detail_l/<int:id>/restore', methods=['PUT'])
    def restore_detail_l(self, id):
        # Здесь будет обработчик для восстановления удаленной детали

if __name__ == '__main__':
    controller = DetailLController()
    app.run(debug=True)

from datetime import datetime
from typing import List
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

Base = declarative_base()

class IdentityCard(Base):
    __tablename__ = 'identity_cards'
    id = Column(Integer, primary_key=True)
    serial = Column(String, nullable=False)
    number = Column(String, nullable=False)
    issuer = Column(String, nullable=False)
    issue_date = Column(DateTime, nullable=False)
    issue_place = Column(String, nullable=False)
    code = Column(String, nullable=False)

class Nextdetail(Base):
    __tablename__ = 'nextdetails'
   
   from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

app = FastAPI()

# Создание всех таблиц в базе данных
models.Base.metadata.create_all(bind=engine)

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для создания нового детали
@app.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

# Маршрут для получения информации о детали по идентификатору
@app.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

# Маршрут для обновления информации о детали
@app.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)

# Маршрут для удаления детали
@app.delete("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.delete_nextdetail(db=db, nextdetail_id=nextdetail_id)

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Nextdetail
@app.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

# Get Nextdetail by ID
@app.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

# Update Nextdetail by ID
@app.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)

# Delete Nextdetail by ID
@app.delete("/nextdetails/{nextdetail_id}")
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    crud.delete_nextdetail(db=db, nextdetail_id=nextdetail_id)
    return {"detail": "Nextdetail deleted"}

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Nextdetail
@app.post("/nextdetail/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

# Get Nextdetail by ID
@app.get("/nextdetail/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

# Update Nextdetail by ID
@app.put("/nextdetail/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)

# Delete Nextdetail by ID
@app.delete("/nextdetail/{nextdetail_id}", response_model=schemas.Nextdetail)
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    crud.delete_nextdetail(db=db, nextdetail_id=nextdetail_id)
    return db_nextdetail

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db, nextdetail)

@app.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

@app.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.update_nextdetail(db, nextdetail_id, nextdetail)

@app.delete("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.delete_nextdetail(db, nextdetail_id)

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

@app.get("/nextdetails/", response_model=List[schemas.Nextdetail])
def read_nextdetails(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nextdetails = crud.get_nextdetails(db, skip=skip, limit=limit)
    return nextdetails

@app.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

@app.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    updated_nextdetail = crud.update_nextdetail(db, nextdetail_id, nextdetail)
    if updated_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return updated_nextdetail

@app.delete("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    deleted_nextdetail = crud.delete_nextdetail(db, nextdetail_id)
    if deleted_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return deleted_nextdetail

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

app = FastAPI()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

@app.get("/nextdetails/", response_model=List[schemas.Nextdetail])
def read_nextdetails(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nextdetails = crud.get_nextdetails(db, skip=skip, limit=limit)
    return nextdetails

@app.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

@app.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    db_nextdetail = crud.update_nextdetail(db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

@app.delete("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.delete_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

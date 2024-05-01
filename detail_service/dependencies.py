from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import dependencies, schemas
from .crud import create_nextdetail, get_nextdetail, get_nextdetails, update_nextdetail, delete_nextdetail

router = APIRouter()


@router.get("/", response_model=List[schemas.Nextdetail])
def read_nextdetails(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    nextdetails = get_nextdetails(db, skip=skip, limit=limit)
    return nextdetails


@router.get("/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(dependencies.get_db)):
    db_nextdetail = get_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail


@router.post("/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(dependencies.get_db)):
    return create_nextdetail(db=db, nextdetail=nextdetail)


@router.put("/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(dependencies.get_db)):
    db_nextdetail = update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail


@router.delete("/{nextdetail_id}", response_model=schemas.Nextdetail)
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(dependencies.get_db)):
    db_nextdetail = delete_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail
python
# dependencies.py

from sqlalchemy.orm import Session
from .crud import get_db
from .database import SessionLocal

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

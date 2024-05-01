from sqlalchemy.orm import Session
from models import Nextdetail
from schemas import NextdetailCreate, NextdetailUpdate
from detail_service import models, schemas

def create_nextdetail(db: Session, nextdetail: schemas.NextdetailCreate):
    db_nextdetail = models.Nextdetail(**nextdetail.dict())
    db.add(db_nextdetail)
    db.commit()
    db.refresh(db_nextdetail)
    return db_nextdetail

def get_nextdetails(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Nextdetail).offset(skip).limit(limit).all()

def get_nextdetail(db: Session, nextdetail_id: int):
    return db.query(models.Nextdetail).filter(models.Nextdetail.id == nextdetail_id).first()

def update_nextdetail(db: Session, nextdetail_id: int, nextdetail: schemas.NextdetailUpdate):
    db_nextdetail = db.query(models.Nextdetail).filter(models.Nextdetail.id == nextdetail_id).first()
    if db_nextdetail:
        db_nextdetail.first_name = nextdetail.first_name
        db_nextdetail.last_name = nextdetail.last_name
        db_nextdetail.birth_date = nextdetail.birth_date
        db_nextdetail.card_id = nextdetail.card_id
        db.commit()
        db.refresh(db_nextdetail)
    return db_nextdetail

def delete_nextdetail(db: Session, nextdetail_id: int):
    db_nextdetail = db.query(models.Nextdetail).filter(models.Nextdetail.id == nextdetail_id).first()
    if db_nextdetail:
        db.delete(db_nextdetail)
        db.commit()
    return db_nextdetail
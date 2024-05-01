from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import crud, models, schemas, security
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    return security.authenticate_user(form_data.username, form_data.password)

@app.get("/nextdetails/", response_model=list[schemas.Nextdetail])
async def read_nextdetails(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nextdetails = crud.get_nextdetails(db, skip=skip, limit=limit)
    return nextdetails

@app.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
async def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

@app.post("/nextdetails/", response_model=schemas.Nextdetail)
async def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

@app.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
async def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    return crud.update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)

@app.delete("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
async def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    return crud.delete_nextdetail(db=db, nextdetail_id=nextdetail_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5432)

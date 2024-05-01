from flask import Blueprint
from .controller import DetailLController
from flask_sqlalchemy import SQLAlchemy
from models import DetailL

app = Flask(__name__)
db = SQLAlchemy(app)

detail_l_bp = Blueprint('detail_l', __name__)

@detail_l_bp.route('/api/detail_l', methods=['POST'])
def add_detail_l():
    return DetailLController().add_detail_l()

@detail_l_bp.route('/api/detail_l', methods=['GET'])
def get_all_detail_ls():
    return DetailLController().get_all_detail_ls()

@detail_l_bp.route('/api/detail_l/<int:id>', methods=['GET'])
def get_detail_l(id):
    return DetailLController().get_detail_l(id)

@detail_l_bp.route('/api/detail_l/<int:id>', methods=['PUT'])
def update_detail_l(id):
    return DetailLController().update_detail_l(id)

@detail_l_bp.route('/api/detail_l/<int:id>', methods=['DELETE'])
def delete_detail_l(id):
    return DetailLController().delete_detail_l(id)

@detail_l_bp.route('/api/detail_l/<int:id>/restore', methods=['PUT'])
def restore_detail_l(id):
    return DetailLController().restore_detail_l(id)

# Ваш код FastAPI остается без изменений
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

from sqlalchemy.orm import Session
from .crud import get_db
from .database import SessionLocal

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from flask import Blueprint
from .controller import DetailLController

detail_l_bp = Blueprint('detail_l', __name__)

@detail_l_bp.route('/api/detail_l', methods=['POST'])
def add_detail_l():
    return DetailLController.add_detail_l()

@detail_l_bp.route('/api/detail_l', methods=['GET'])
def get_all_detail_ls():
    return DetailLController.get_all_detail_ls()

@detail_l_bp.route('/api/detail_l/<int:id>', methods=['GET'])
def get_detail_l(id):
    return DetailLController.get_detail_l(id)

@detail_l_bp.route('/api/detail_l/<int:id>', methods=['PUT'])
def update_detail_l(id):
    return DetailLController.update_detail_l(id)

@detail_l_bp.route('/api/detail_l/<int:id>', methods=['DELETE'])
def delete_detail_l(id):
    return DetailLController.delete_detail_l(id)

@detail_l_bp.route('/api/detail_l/<int:id>/restore', methods=['PUT'])
def restore_detail_l(id):
    return DetailLController.restore_detail_l(id)

from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal, engine

# Инициализация миграций
Base.metadata.create_all(bind=engine)

router = APIRouter()

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

@router.get("/nextdetails/", response_model=List[schemas.Nextdetail])
def read_nextdetails(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nextdetails = crud.get_nextdetails(db, skip=skip, limit=limit)
    return nextdetails

@router.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

@router.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    return crud.update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)

@router.delete("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    return crud.delete_nextdetail(db=db, nextdetail_id=nextdetail_id)
    
from typing import List
from fastapi import APIRouter, HTTPException, Path
from . import schemas

router = APIRouter()

# Здесь должны быть маршруты для операций CRUD (create, read, update, delete) сущностей Nextdetail
# Пример:

@router.post("/nextdetails/", response_model=schemas.NextdetailGetResponse)
async def create_nextdetail(nextdetail: schemas.NextdetailCreateRequest):
    # Логика для создания новой записи о следующем детализировании
    pass

@router.get("/nextdetails/", response_model=List[schemas.NextdetailGetResponse])
async def read_nextdetails():
    # Логика для чтения списка записей о следующем детализировании
    pass

@router.get("/nextdetails/{nextdetail_id}", response_model=schemas.NextdetailGetResponse)
async def read_nextdetail(nextdetail_id: int = Path(..., title="The ID of the nextdetail to get")):
    # Логика для чтения отдельной записи о следующем детализировании по ее ID
    pass

@router.put("/nextdetails/{nextdetail_id}", response_model=schemas.NextdetailGetResponse)
async def update_nextdetail(nextdetail_id: int = Path(..., title="The ID of the nextdetail to update"), nextdetail: schemas.NextdetailUpdateRequest):
    # Логика для обновления записи о следующем детализировании
    pass

@router.delete("/nextdetails/{nextdetail_id}", response_model=schemas.NextdetailGetResponse)
async def delete_nextdetail(nextdetail_id: int = Path(..., title="The ID of the nextdetail to delete")):
    # Логика для удаления записи о следующем детализировании
    pass

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..database import SessionLocal, engine

# Создаем экземпляр APIRouter
router = APIRouter()

# Функция для получения экземпляра базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Маршрут для создания новой детали
@router.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

# Маршрут для получения всех деталей
@router.get("/nextdetails/", response_model=List[schemas.Nextdetail])
def read_nextdetails(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    nextdetails = crud.get_nextdetails(db, skip=skip, limit=limit)
    return nextdetails

# Маршрут для получения детали по ее ID
@router.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

# Маршрут для обновления детали
@router.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    return crud.update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)

# Маршрут для удаления детали
@router.delete("/nextdetails/{nextdetail_id}")
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    return crud.delete_nextdetail(db=db, nextdetail_id=nextdetail_id)

# Определение маршрута для создания следующего детализирования
@app.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

# Определение маршрута для чтения следующего детализирования по его идентификатору
@app.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

# Определение маршрута для обновления следующего детализирования
@app.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    return crud.update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)

# Определение маршрута для удаления следующего детализирования
@app.delete("/nextdetails/{nextdetail_id}")
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    return crud.delete_nextdetail(db=db, nextdetail_id=nextdetail_id)

# Определение маршрута для восстановления следующего детализирования
@app.put("/nextdetails/{nextdetail_id}/restore", response_model=schemas.Nextdetail)
def restore_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    return crud.restore_nextdetail(db=db, nextdetail_id=nextdetail_id)

# Валидатор запроса на обновление следующего детализирования
class NextdetailUpdateRequestValidator(BaseModel):
    first_name: str
    last_name: str
    birth_date: date

    @root_validator
    def validate_birth_date(cls, values):
        if values.get("birth_date") > date.today() - timedelta(days=365 * 14):
            raise ValueError("Minimum nextdetail age is 14 years")
        return values

# Определение маршрута для обновления следующего детализирования
@app.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)

# Импорты
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import schemas, crud, models
from .database import SessionLocal

# Создаем экземпляр APIRouter
router = APIRouter()

# Функция для получения экземпляра сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Определение маршрутов для работы с Nextdetail
@router.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

@router.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

@router.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.update_nextdetail(db=db, nextdetail_id=nextdetail_id, nextdetail=nextdetail)

@router.delete("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.delete_nextdetail(db=db, nextdetail_id=nextdetail_id)

@router.put("/nextdetails/{nextdetail_id}/restore", response_model=schemas.Nextdetail)
def restore_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_deleted_nextdetail(db=db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Deleted Nextdetail not found")
    return crud.restore_nextdetail(db=db, nextdetail_id=nextdetail_id)
    
# Импорт необходимых модулей
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from . import schemas, crud
from .database import SessionLocal
from .dependencies import get_db

# Определение маршрутов для работы с Nextdetail
@app.get("/nextdetails", response_model=List[schemas.Nextdetail])
def read_nextdetails(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nextdetails = crud.get_nextdetails(db, skip=skip, limit=limit)
    return nextdetails

@app.get("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def read_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return db_nextdetail

# Импорт необходимых модулей
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from . import schemas, crud
from .database import SessionLocal
from .dependencies import get_db

# Определение маршрутов для работы с Nextdetail
@app.post("/nextdetails/", response_model=schemas.Nextdetail)
def create_nextdetail(nextdetail: schemas.NextdetailCreate, db: Session = Depends(get_db)):
    return crud.create_nextdetail(db=db, nextdetail=nextdetail)

@app.put("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def update_nextdetail(nextdetail_id: int, nextdetail: schemas.NextdetailUpdate, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.update_nextdetail(db=db, nextdetail=nextdetail, nextdetail_id=nextdetail_id)

@app.delete("/nextdetails/{nextdetail_id}", response_model=schemas.Nextdetail)
def delete_nextdetail(nextdetail_id: int, db: Session = Depends(get_db)):
    db_nextdetail = crud.get_nextdetail(db, nextdetail_id=nextdetail_id)
    if db_nextdetail is None:
        raise HTTPException(status_code=404, detail="Nextdetail not found")
    return crud.delete_nextdetail(db=db, nextdetail_id=nextdetail_id)    

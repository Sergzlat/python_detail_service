from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from detail_service import models  # Предполагается, что модели находятся в папке detail_service

# Подключение к базе данных
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/db_name"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Используем declarative_base() для создания базового класса моделей
Base = declarative_base()

# Здесь может быть ваш код с определением схем и контроллеров

# После того, как у вас определены все модели, вы можете создать таблицы в базе данных
Base.metadata.create_all(bind=engine)

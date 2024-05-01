from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum
from datetime import datetime
from database import Base

Base = declarative_base()

class UserType(Enum):
    Unknown = 0
    Nextdetail = 1
    DetailL = 2
    Admin = 3

class DetailL(Base):
    __tablename__ = 'detail_ls'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    email = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)

    def __init__(self, first_name, middle_name, last_name, birth_date, email):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email
        self.is_deleted = False

class IdentityCard(Base):
    __tablename__ = "identitycards"

    id = Column(Integer, primary_key=True, index=True)
    serial = Column(String, index=True)
    number = Column(String, index=True)
    issuer = Column(String, index=True)
    issue_date = Column(DateTime)
    issue_place = Column(String)
    code = Column(String)

    nextdetail_id = Column(Integer, ForeignKey("nextdetails.id"))
    nextdetail = relationship("Nextdetail", back_populates="identity_card")

class Nextdetail(Base):
    __tablename__ = "nextdetails"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    birth_date = Column(DateTime)
    card_id = Column(String)
    is_deleted = Column(Boolean, default=False)

    identity_card_id = Column(Integer, ForeignKey("identitycards.id"))
    identity_card = relationship("IdentityCard", back_populates="nextdetails")

class Entity(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    is_deleted = Column(Boolean, default=False)
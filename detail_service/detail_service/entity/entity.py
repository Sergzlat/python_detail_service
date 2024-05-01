from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DetailL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"DetailL('{self.first_name}', '{self.last_name}', '{self.email}')"

from .database import db

class DetailL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"DetailL(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, birth_date={self.birth_date})"
 
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class DetailL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    is_deleted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"DetailL('{self.first_name}', '{self.last_name}', '{self.email}')"

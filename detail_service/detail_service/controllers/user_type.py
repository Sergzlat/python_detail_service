from typing import List
from enum import Enum
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

Base = declarative_base()

class UserType(Enum):
    Unknown = 0
    Nextdetail = 1
    DetailL = 2
    Admin = 3

class Entity:
    def __init__(self):
        self.id = None
        self.is_deleted = False

class DetailL(Entity, Base):
    __tablename__ = 'detail_ls'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    email = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)

    def __init__(self, first_name, middle_name, last_name, birth_date, email):
        super().__init__()
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email
        self.is_deleted = False

class DetailLController:
    def __init__(self):
        self.mapper = None
        self.context = DetailLContext()
        self.user_service = None

    @app.route('/api/detail_l', methods=['POST'])
    def add_detail_l(self):
        request_data = request.json
        detail_l = self.mapper.map(request_data, DetailL)
        self.context.add_detail_l(detail_l)
        return jsonify(self.mapper.map(detail_l, DetailLResponse)), 201

    @app.route('/api/detail_l', methods=['GET'])
    def get_all_detail_ls(self):
        detail_ls = self.context.get_all_detail_ls()
        return jsonify([self.mapper.map(detail_l, DetailLResponse) for detail_l in detail_ls])

    @app.route('/api/detail_l/<int:id>', methods=['GET'])
    def get_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            return jsonify(self.mapper.map(detail_l, DetailLResponse))
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    @app.route('/api/detail_l/<int:id>', methods=['PUT'])
    def update_detail_l(self, id):
        request_data = request.json
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            self.mapper.map(request_data, detail_l)
            self.context.save_changes()
            return '', 204
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    @app.route('/api/detail_l/<int:id>', methods=['DELETE'])
    def delete_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            self.context.delete_detail_l(detail_l)
            return '', 204
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    @app.route('/api/detail_l/<int:id>/restore', methods=['PUT'])
    def restore_detail_l(self, id):
        detail_l = self.context.get_deleted_detail_l(id)
        if detail_l:
            detail_l.is_deleted = False
            self.context.save_changes()
            return jsonify(self.mapper.map(detail_l, DetailLResponse))
        else:
            return jsonify({'message': 'Deleted DetailL not found'}), 404

if __name__ == '__main__':
    controller = DetailLController()
    app.run(debug=True)
    
from typing import Optional
import aiohttp

from enum import Enum
from dataclasses import dataclass

class UserType(Enum):
    Nextdetail = 1

@dataclass
class SignUpResponse:
    Id: int
    Email: str
    Message: str

class UserService:
    def __init__(self, auth_service_connection: str):
        self._auth_service_connection = auth_service_connection

    async def create_user(self, email: str, password: str) -> Optional[SignUpResponse]:
        payload = {
            "Email": email,
            "Password": password,
            "Type": str(UserType.Nextdetail.value),
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self._auth_service_connection}/signup", data=payload) as response:
                if response.status != 200:
                    return None
                data = await response.json()
                return SignUpResponse(**data)
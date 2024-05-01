from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy_utils import ArrowType
from enum import Enum

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

class Entity:
    def __init__(self):
        pass

def get_symmetric_security_key():
    pass

class AuthOptions:
    Issuer = ""
    Audience = ""

def add_detail_l_services(services, builder):
    return (services
            .add_database(builder)
            .add_automapper()
            .add_validation()
            .add_jwt_authentication()
            .add_swagger_generator()
            .add_user_service())

def add_database(services, builder):
    return services.add('DetailLContext', lambda: DetailLContext(builder))

def add_automapper(services):
    return services

def add_validation(services):
    return services

def add_user_service(services):
    return services.add('UserService', UserService)

def add_jwt_authentication(services):
    return services

def add_swagger_generator(services):
    return services

from .models import DetailL

class DetailLService:
    def __init__(self, context, mapper):
        self.context = context
        self.mapper = mapper

    def add_detail_l(self, request_data):
        detail_l = self.mapper.map(request_data, DetailL())
        self.context.add_detail_l(detail_l)
        return detail_l

    def get_all_detail_ls(self):
        return self.context.get_all_detail_ls()

    def get_detail_l(self, id):
        return self.context.get_detail_l(id)

    def update_detail_l(self, id, request_data):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            self.mapper.map(request_data, detail_l)
            self.context.save_changes()
        return detail_l

    def delete_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            self.context.delete_detail_l(detail_l)
        return detail_l

    def restore_detail_l(self, id):
        detail_l = self.context.get_deleted_detail_l(id)
        if detail_l:
            detail_l.is_deleted = False
            self.context.save_changes()
        return detail_l

from models import DetailLContext, DetailL
from mappers import Mapper

class DetailLService:
    def __init__(self):
        self.context = DetailLContext()
        self.mapper = Mapper()

    def add_detail_l(self, request_data):
        detail_l = self.mapper.map(request_data, DetailL)
        self.context.add_detail_l(detail_l)

    def get_all_detail_ls(self):
        detail_ls = self.context.get_all_detail_ls()
        return [self.mapper.map(detail_l, DetailLResponse) for detail_l in detail_ls]

    def get_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            return self.mapper.map(detail_l, DetailLResponse)
        else:
            return {'message': 'DetailL not found'}

    def update_detail_l(self, id, request_data):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            self.mapper.map(request_data, detail_l)
            self.context.save_changes()

    def delete_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            self.context.delete_detail_l(detail_l)

from models import DetailL

class DetailLService:
    def __init__(self):
        pass

    def add_detail_l(self, data):
        detail_l = DetailL(**data)
        detail_l.save()

    def get_all_detail_ls(self):
        return DetailL.objects().all()

    def get_detail_l(self, id):
        return DetailL.objects(id=id).first()

    def update_detail_l(self, id, data):
        detail_l = self.get_detail_l(id)
        for key, value in data.items():
            setattr(detail_l, key, value)
        detail_l.save()

    def delete_detail_l(self, id):
        detail_l = self.get_detail_l(id)
        detail_l.delete()

    def restore_detail_l(self, id):
        detail_l = self.get_deleted_detail_l(id)
        detail_l.is_deleted = False
        detail_l.save()
        return detail_l

from models import DetailL

class DetailLService:
    def add_detail_l(self, data):
        detail_l = DetailL(**data)
        detail_l.save()

    def get_all_detail_ls(self):
        return DetailL.objects.all()

    def get_detail_l(self, id):
        return DetailL.objects(id=id).first()

    def update_detail_l(self, id, data):
        DetailL.objects(id=id).update(**data)

    def delete_detail_l(self, id):
        DetailL.objects(id=id).delete()

    def restore_detail_l(self, id):
        restored_detail_l = DetailL.objects(id=id, is_deleted=True).first()
        if restored_detail_l:
            restored_detail_l.is_deleted = False
            restored_detail_l.save()
        return restored_detail_l.to_json()

from models import DetailL

class DetailLService:
    def add_detail_l(self, data):
        detail_l = DetailL(**data)
        detail_l.save()

    def get_all_detail_ls(self):
        return DetailL.query.all()

    def get_detail_l(self, id):
        return DetailL.query.get(id)

    def update_detail_l(self, id, data):
        detail_l = self.get_detail_l(id)
        if detail_l:
            detail_l.update(data)

    def delete_detail_l(self, id):
        detail_l = self.get_detail_l(id)
        if detail_l:
            detail_l.delete()

    def restore_detail_l(self, id):
        deleted_detail_l = self.get_deleted_detail_l(id)
        if deleted_detail_l:
            deleted_detail_l.is_deleted = False
            deleted_detail_l.save()
            return deleted_detail_l
        else:
            return None

from models import DetailL
from validators import DetailLValidator
from datetime import datetime

class DetailLService:
    def __init__(self, context):
        self.context = context

    def add_detail_l(self, data):
        errors = DetailLValidator.validate_detail_l(data)
        if errors:
            return errors, None

        detail_l = DetailL(
            first_name=data['first_name'],
            last_name=data['last_name'],
            birth_date=datetime.strptime(data['birth_date'], '%Y-%m-%d')
        )

        self.context.add_detail_l(detail_l)
        return None, detail_l

    def get_all_detail_ls(self):
        return self.context.get_all_detail_ls()

    def get_detail_l(self, id):
        return self.context.get_detail_l(id)

    def update_detail_l(self, id, data):
        detail_l = self.context.get_detail_l(id)
        if not detail_l:
            return "DetailL not found", None

        errors = DetailLValidator.validate_detail_l(data)
        if errors:
            return errors, None

        detail_l.first_name = data['first_name']
        detail_l.last_name = data['last_name']
        detail_l.birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')

        self.context.save_changes()
        return None, detail_l

    def delete_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if not detail_l:
            return "DetailL not found", None

        self.context.delete_detail_l(detail_l)
        return None, None

    def restore_detail_l(self, id):
        detail_l = self.context.get_deleted_detail_l(id)
        if not detail_l:
            return "Deleted DetailL not found", None

        detail_l.is_deleted = False
        self.context.save_changes()
        return None, detail_l

from models import DetailL

class DetailLService:
    def __init__(self, context):
        self.context = context

    def add_detail_l(self, data):
        detail_l = DetailL(**data)
        self.context.add_detail_l(detail_l)
        return None, detail_l

    def get_all_detail_ls(self):
        return self.context.get_all_detail_ls()

    def get_detail_l(self, id):
        return self.context.get_detail_l(id)

    def update_detail_l(self, id, data):
        detail_l = self.context.get_detail_l(id)
        if not detail_l:
            return 'DetailL not found', None

        for key, value in data.items():
            setattr(detail_l, key, value)

        return None, detail_l

    def delete_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if not detail_l:
            return 'DetailL not found', None

        detail_l.is_deleted = True
        return None, detail_l

    def restore_detail_l(self, id):
        detail_l = self.context.get_deleted_detail_l(id)
        if not detail_l:
            return 'Deleted DetailL not found', None

        detail_l.is_deleted = False
        return None, detail_l

from models import DetailL

class DetailLService:
    def __init__(self, context):
        self.context = context

    def add_detail_l(self, data):
        detail_l = DetailL(**data)
        self.context.add(detail_l)
        self.context.commit()
        return None, detail_l

    def get_all_detail_ls(self):
        return self.context.query(DetailL).all()

    def get_detail_l(self, id):
        return self.context.query(DetailL).filter_by(id=id).first()

    def update_detail_l(self, id, data):
        detail_l = self.get_detail_l(id)
        if not detail_l:
            return 'DetailL not found', None
        for key, value in data.items():
            setattr(detail_l, key, value)
        self.context.commit()
        return None, detail_l

    def delete_detail_l(self, id):
        detail_l = self.get_detail_l(id)
        if not detail_l:
            return 'DetailL not found', None
        self.context.delete(detail_l)
        self.context.commit()
        return None, None

    def restore_detail_l(self, id):
        detail_l = self.context.query(DetailL).with_deleted().filter_by(id=id).first()
        if not detail_l:
            return 'Deleted DetailL not found', None
        detail_l.is_deleted = False
        self.context.commit()
        return None, detail_l

from typing import List
from .exceptions import DetailLNotFoundException, DeletedDetailLNotFoundException
from .models import DetailL


class DetailLService:
    def __init__(self, context, mapper):
        self.context = context
        self.mapper = mapper

    def add_detail_l(self, request_data):
        detail_l = self.mapper.map(request_data, DetailL)
        self.context.add_detail_l(detail_l)
        return detail_l

    def get_all_detail_ls(self):
        return self.context.get_all_detail_ls()

    def get_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            return detail_l
        else:
            raise DetailLNotFoundException()

    def update_detail_l(self, id, request_data):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            self.mapper.map(request_data, detail_l)
            self.context.save_changes()
        else:
            raise DetailLNotFoundException()

    def delete_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            self.context.delete_detail_l(detail_l)
        else:
            raise DetailLNotFoundException()

    def restore_detail_l(self, id):
        detail_l = self.context.get_deleted_detail_l(id)
        if detail_l:
            detail_l.is_deleted = False
            self.context.save_changes()
            return detail_l
        else:
            raise DeletedDetailLNotFoundException()

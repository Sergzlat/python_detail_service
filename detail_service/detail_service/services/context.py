from typing import List
from .exceptions import DetailLNotFoundException, DeletedDetailLNotFoundException
from .models import DetailL

class DetailLContext:
    def __init__(self):
        self.detail_ls = []

    def add_detail_l(self, detail_l: DetailL):
        self.detail_ls.append(detail_l)

    def get_all_detail_ls(self) -> List[DetailL]:
        return self.detail_ls

    def get_detail_l(self, id: int) -> DetailL:
        for detail_l in self.detail_ls:
            if detail_l.id == id:
                return detail_l
        raise DetailLNotFoundException()

    def delete_detail_l(self, detail_l: DetailL):
        self.detail_ls.remove(detail_l)

    def get_deleted_detail_l(self, id: int) -> DetailL:
        for detail_l in self.detail_ls:
            if detail_l.id == id and detail_l.is_deleted:
                return detail_l
        raise DeletedDetailLNotFoundException()

    def save_changes(self):
        pass  # Placeholder for saving changes to the database

from models import DetailL, db

class DetailLContext:
    def add_detail_l(self, detail_l):
        db.session.add(detail_l)
        db.session.commit()

    def get_all_detail_ls(self):
        return DetailL.query.filter_by(is_deleted=False).all()

    def get_detail_l(self, id):
        return DetailL.query.filter_by(id=id, is_deleted=False).first()

    def delete_detail_l(self, detail_l):
        db.session.delete(detail_l)
        db.session.commit()

from datetime import datetime
from typing import List

class DetailLContext:
    def __init__(self):
        self.detail_ls = []

    def add_detail_l(self, detail_l):
        self.detail_ls.append(detail_l)

    def get_all_detail_ls(self):
        return self.detail_ls

    def get_detail_l(self, id):
        for detail_l in self.detail_ls:
            if detail_l.id == id:
                return detail_l
        return None

    def save_changes(self):
        pass

    def delete_detail_l(self, detail_l):
        self.detail_ls.remove(detail_l)

    def get_deleted_detail_l(self, id):
        for detail_l in self.detail_ls:
            if detail_l.id == id and detail_l.is_deleted:
                return detail_l
        return None

from .entity import DetailL
from .database import db

class DetailLContext:
    def add_detail_l(self, detail_l):
        db.session.add(detail_l)
        db.session.commit()

    def get_all_detail_ls(self):
        return DetailL.query.filter_by(is_deleted=False).all()

    def get_detail_l(self, id):
        return DetailL.query.get(id)

    def save_changes(self):
        db.session.commit()

    def delete_detail_l(self, detail_l):
        db.session.delete(detail_l)
        db.session.commit()

    def get_deleted_detail_l(self, id):
        return DetailL.query.filter_by(id=id, is_deleted=True).first()

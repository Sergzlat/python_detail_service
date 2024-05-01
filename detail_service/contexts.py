from .models import db, DetailL

class DetailLContext:
    def add_detail_l(self, detail_l):
        db.session.add(detail_l)
        db.session.commit()

    def get_all_detail_ls(self):
        return DetailL.query.all()

    def get_detail_l(self, id):
        return DetailL.query.get(id)

    def save_changes(self):
        db.session.commit()

    def delete_detail_l(self, detail_l):
        db.session.delete(detail_l)
        db.session.commit()

    def get_deleted_detail_l(self, id):
        return DetailL.query.filter_by(id=id, is_deleted=True).first()

from .models import DetailL

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

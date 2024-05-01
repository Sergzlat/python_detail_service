from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class DetailLContext:
    def __init__(self):
        self.engine = create_engine('sqlite:///app.db')
        self.Session = sessionmaker(bind=self.engine)

    def add_detail_l(self, detail_l):
        session = self.Session()
        session.add(detail_l)
        session.commit()
        session.close()

    def get_all_detail_ls(self):
        session = self.Session()
        detail_ls = session.query(DetailL).all()
        session.close()
        return detail_ls

    def get_detail_l(self, id):
        session = self.Session()
        detail_l = session.query(DetailL).filter_by(id=id).first()
        session.close()
        return detail_l

    def save_changes(self):
        session = self.Session()
        session.commit()
        session.close()

    def delete_detail_l(self, detail_l):
        session = self.Session()
        session.delete(detail_l)
        session.commit()
        session.close()

    def get_deleted_detail_l(self, id):
        session = self.Session()
        detail_l = session.query(DetailL).filter_by(id=id, is_deleted=True).first()
        session.close()
        return detail_l

class DetailLResponse:
    def __init__(self, id, first_name, middle_name, last_name, birth_date, email):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email

class UserService:
    def __init__(self):
        pass


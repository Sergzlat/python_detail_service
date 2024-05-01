from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

def get_session():
    engine = create_engine('sqlite:///detailL.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def handle_classification(request, error):
    pass

def load_data():
    pass

def save_data():
    pass

def action_change():
    pass

def scale_image(image, size):
    pass

def recognize(sender):
    pass

def recognize_detail():
    pass

def get_file_name(url, name):
    pass

def file_exists(url, name):
    pass

def get_documents_directory():
    pass

def json_from_object(rect):
    pass

def view_did_load():
    pass

def view_will_disappear(animated):
    pass

def setup_image_scroll_view():
    pass

def matrix_to_arr(matrix):
    pass

def transp(array):
    pass
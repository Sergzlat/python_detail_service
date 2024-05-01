from flask import request, jsonify
from mapper import Mapper
from detail_l_context import DetailLContext
from flask_sqlalchemy import SQLAlchemy
from models import DetailL

app = Flask(__name__)
db = SQLAlchemy(app)

class DetailLController:
    def __init__(self):
        self.mapper = Mapper()
        self.context = DetailLContext()

    @app.route('/api/detail_l', methods=['POST'])
    def add_detail_l(self):
        # Метод add_detail_l из оригинального кода

    @app.route('/api/detail_l', methods=['GET'])
    def get_all_detail_ls(self):
        # Метод get_all_detail_ls из оригинального кода

    # Другие методы контроллера

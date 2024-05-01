from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify
from models import DetailL
from services import DetailLService
from mappers import DetailLMapper

app = Flask(__name__)
db = SQLAlchemy(app)

class DetailLController:
    def __init__(self):
        self.service = DetailLService()
        self.mapper = DetailLMapper()

    @app.route('/api/detail_l', methods=['GET'])
    def get_detail_l():
        detail_l = self.service.get_detail_l()
        return jsonify(self.mapper.map(detail_l, DetailLResponse)), 201

class DetailLController:
    def __init__(self, context):
        self.service = DetailLService(context)
        self.mapper = DetailLMapper()

    def add_detail_l(self):
        request_data = request.json
        errors, detail_l = self.service.add_detail_l(request_data)
        if errors:
            return jsonify(errors), 400

        return jsonify(self.mapper.map_to_response(detail_l)), 201

    def get_all_detail_ls(self):
        detail_ls = self.service.get_all_detail_ls()
        return jsonify([self.mapper.map_to_response(detail_l) for detail_l in detail_ls])

    def get_detail_l(self, id):
        detail_l = self.service.get_detail_l(id)
        if not detail_l:
            return jsonify({'message': 'DetailL not found'}), 404

        return jsonify(self.mapper.map_to_response(detail_l))

    def update_detail_l(self, id):
        request_data = request.json
        errors, detail_l = self.service.update_detail_l(id, request_data)
        if errors:
            return jsonify(errors), 400

        if not detail_l:
            return '', 204

        return jsonify(self.mapper.map_to_response(detail_l))

    def delete_detail_l(self, id):
        errors, _ = self.service.delete_detail_l(id)
        if errors:
            return jsonify({'message': errors}), 404

        return '', 204

    def restore_detail_l(self, id):
        errors, detail_l = self.service.restore_detail_l(id)
        if errors:
            return jsonify({'message': errors}), 404

        return jsonify(self.mapper.map_to_response(detail_l))

from flask import Flask, request, jsonify
from .models import DetailL
from .mappers import Mapper
from .contexts import DetailLContext

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class DetailLController:
    def __init__(self):
        self.mapper = Mapper()
        self.context = DetailLContext()

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

from flask import request, jsonify
from .services import DetailLService
from .mappers import Mapper
from .contexts import DetailLContext

class DetailLController:
    def __init__(self):
        self.service = DetailLService(DetailLContext(), Mapper())

    def add_detail_l(self):
        request_data = request.json
        detail_l = self.service.add_detail_l(request_data)
        return jsonify(self.mapper.map(detail_l, DetailLResponse)), 201

    def get_all_detail_ls(self):
        detail_ls = self.service.get_all_detail_ls()
        return jsonify([self.mapper.map(detail_l, DetailLResponse) for detail_l in detail_ls])

    def get_detail_l(self, id):
        detail_l = self.service.get_detail_l(id)
        if detail_l:
            return jsonify(self.mapper.map(detail_l, DetailLResponse))
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    def update_detail_l(self, id):
        request_data = request.json
        detail_l = self.service.update_detail_l(id, request_data)
        if detail_l:
            return '', 204
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    def delete_detail_l(self, id):
        detail_l = self.service.delete_detail_l(id)
        if detail_l:
            return '', 204
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    def restore_detail_l(self, id):
        detail_l = self.service.restore_detail_l(id)
        if detail_l:
            return jsonify(self.mapper.map(detail_l, DetailLResponse))
        else:
            return jsonify({'message': 'Deleted DetailL not found'}), 404

from flask import jsonify
from models import DetailL, db

class DetailLController:
    def __init__(self):
        self.context = DetailLContext()

    def add_detail_l(self, request_data):
        detail_l = DetailL(**request_data)
        self.context.add_detail_l(detail_l)
        return jsonify(detail_l), 201

    def get_all_detail_ls(self):
        detail_ls = self.context.get_all_detail_ls()
        return jsonify(detail_ls)

    def get_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            return jsonify(detail_l)
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    def update_detail_l(self, id, request_data):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            detail_l.update(request_data)
            db.session.commit()
            return '', 204
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    def delete_detail_l(self, id):
        detail_l = self.context.get_detail_l(id)
        if detail_l:
            self.context.delete_detail_l(detail_l)
            return '', 204
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    def restore_detail_l(self, id):
        detail_l = self.context.get_deleted_detail_l(id)
        if detail_l:
            detail_l.is_deleted = False
            db.session.commit()
            return jsonify(detail_l)
        else:
            return jsonify({'message': 'Deleted DetailL not found'}), 404

from flask import request, jsonify
from services import DetailLService

class DetailLController:
    def __init__(self):
        self.service = DetailLService()

    def add_detail_l(self):
        request_data = request.json
        self.service.add_detail_l(request_data)
        return jsonify(self.service.get_detail_l(detail_l.id)), 201

    def get_all_detail_ls(self):
        return jsonify(self.service.get_all_detail_ls())

    def get_detail_l(self, id):
        return jsonify(self.service.get_detail_l(id))

    def update_detail_l(self, id):
        request_data = request.json
        self.service.update_detail_l(id, request_data)
        return '', 204

    def delete_detail_l(self, id):
        self.service.delete_detail_l(id)
        return '', 204

    def restore_detail_l(self, id):
        detail_l = self.service.restore_detail_l(id)
        return jsonify(detail_l)

from flask import jsonify, request
from flask.views import MethodView
from services import DetailLService

class DetailLAPI(MethodView):
    def __init__(self):
        self.service = DetailLService()

    def post(self):
        data = request.json
        self.service.add_detail_l(data)
        return jsonify(data), 201

    def get(self, id=None):
        if id is None:
            detail_ls = self.service.get_all_detail_ls()
            return jsonify(detail_ls)
        else:
            detail_l = self.service.get_detail_l(id)
            if detail_l:
                return jsonify(detail_l)
            else:
                return jsonify({'message': 'DetailL not found'}), 404

    def put(self, id):
        data = request.json
        self.service.update_detail_l(id, data)
        return '', 204

    def delete(self, id):
        self.service.delete_detail_l(id)
        return '', 204

class DetailLRestoreAPI(MethodView):
    def __init__(self):
        self.service = DetailLService()

    def put(self, id):
        restored_detail_l = self.service.restore_detail_l(id)
        return jsonify(restored_detail_l)

from flask import request, jsonify
from services import DetailLService
from models import DetailL

detail_l_service = DetailLService()

def add_detail_l():
    data = request.json
    detail_l_service.add_detail_l(data)
    return jsonify({'message': 'DetailL added successfully'}), 201

def get_all_detail_ls():
    detail_ls = detail_l_service.get_all_detail_ls()
    return jsonify([detail_l.to_json() for detail_l in detail_ls])

def get_detail_l(id):
    detail_l = detail_l_service.get_detail_l(id)
    if detail_l:
        return jsonify(detail_l.to_json())
    else:
        return jsonify({'message': 'DetailL not found'}), 404

def update_detail_l(id):
    data = request.json
    detail_l_service.update_detail_l(id, data)
    return jsonify({'message': 'DetailL updated successfully'}), 200

def delete_detail_l(id):
    detail_l_service.delete_detail_l(id)
    return jsonify({'message': 'DetailL deleted successfully'}), 204

def restore_detail_l(id):
    restored_detail_l = detail_l_service.restore_detail_l(id)
    if restored_detail_l:
        return jsonify(restored_detail_l)
    else:
        return jsonify({'message': 'Deleted DetailL not found'}), 404

from flask import request, jsonify
from models import DetailL
from services import DetailLService
from mappers import DetailLMapper

class DetailLController:
    def __init__(self, context):
        self.service = DetailLService(context)
        self.mapper = DetailLMapper()

    def add_detail_l(self):
        request_data = request.json
        errors, detail_l = self.service.add_detail_l(request_data)
        if errors:
            return jsonify(errors), 400

        return jsonify(self.mapper.map_to_response(detail_l)), 201

    def get_all_detail_ls(self):
        detail_ls = self.service.get_all_detail_ls()
        return jsonify([self.mapper.map_to_response(detail_l) for detail_l in detail_ls])

    def get_detail_l(self, id):
        detail_l = self.service.get_detail_l(id)
        if not detail_l:
            return jsonify({'message': 'DetailL not found'}), 404

        return jsonify(self.mapper.map_to_response(detail_l))

    def update_detail_l(self, id):
        request_data = request.json
        errors, detail_l = self.service.update_detail_l(id, request_data)
        if errors:
            return jsonify(errors), 400

        if not detail_l:
            return '', 204

        return jsonify(self.mapper.map_to_response(detail_l))

    def delete_detail_l(self, id):
        errors, _ = self.service.delete_detail_l(id)
        if errors:
            return jsonify({'message': errors}), 404

        return '', 204

    def restore_detail_l(self, id):
        errors, detail_l = self.service.restore_detail_l(id)
        if errors:
            return jsonify({'message': errors}), 404

        return jsonify(self.mapper.map_to_response(detail_l))

from flask import request, jsonify
from mappers import Mapper
from services import DetailLService

class DetailLController:
    def __init__(self, context):
        self.mapper = Mapper()
        self.service = DetailLService(context)

    def add_detail_l(self):
        request_data = request.json
        error, detail_l = self.service.add_detail_l(request_data)
        if error:
            return jsonify({'message': error}), 400
        return jsonify(self.mapper.map(detail_l)), 201

    def get_all_detail_ls(self):
        detail_ls = self.service.get_all_detail_ls()
        return jsonify([self.mapper.map(detail_l) for detail_l in detail_ls])

    def get_detail_l(self, id):
        detail_l = self.service.get_detail_l(id)
        if not detail_l:
            return jsonify({'message': 'DetailL not found'}), 404
        return jsonify(self.mapper.map(detail_l))

    def update_detail_l(self, id):
        request_data = request.json
        error, detail_l = self.service.update_detail_l(id, request_data)
        if error:
            return jsonify({'message': error}), 404
        return '', 204

    def delete_detail_l(self, id):
        error, _ = self.service.delete_detail_l(id)
        if error:
            return jsonify({'message': error}), 404
        return '', 204

    def restore_detail_l(self, id):
        error, detail_l = self.service.restore_detail_l(id)
        if error:
            return jsonify({'message': error}), 404
        return jsonify(self.mapper.map(detail_l))

from flask import Flask, request, jsonify
from .models import DetailL
from .context import DetailLContext
from .mapper import Mapper
from .responses import DetailLResponse
from .exceptions import DetailLNotFoundException, DeletedDetailLNotFoundException

app = Flask(__name__)

class DetailLController:
    def __init__(self):
        self.mapper = Mapper()
        self.context = DetailLContext()

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
        try:
            detail_l = self.context.get_detail_l(id)
            return jsonify(self.mapper.map(detail_l, DetailLResponse))
        except DetailLNotFoundException as e:
            return jsonify({'message': e.message}), 404

    @app.route('/api/detail_l/<int:id>', methods=['PUT'])
    def update_detail_l(self, id):
        request_data = request.json
        try:
            detail_l = self.context.get_detail_l(id)
            self.mapper.map(request_data, detail_l)
            self.context.save_changes()
            return '', 204
        except DetailLNotFoundException as e:
            return jsonify({'message': e.message}), 404

    @app.route('/api/detail_l/<int:id>', methods=['DELETE'])
    def delete_detail_l(self, id):
        try:
            detail_l = self.context.get_detail_l(id)
            self.context.delete_detail_l(detail_l)
            return '', 204
        except DetailLNotFoundException as e:
            return jsonify({'message': e.message}), 404

    @app.route('/api/detail_l/<int:id>/restore', methods=['PUT'])
    def restore_detail_l(self, id):
        try:
            detail_l = self.context.get_deleted_detail_l(id)
            detail_l.is_deleted = False
            self.context.save_changes()
            return jsonify(self.mapper.map(detail_l, DetailLResponse))
        except DeletedDetailLNotFoundException as e:
            return jsonify({'message': e.message}), 404

if __name__ == '__main__':
    controller = DetailLController()
    app.run(debug=True)

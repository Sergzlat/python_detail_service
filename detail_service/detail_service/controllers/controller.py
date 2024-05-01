from flask import jsonify, request
from .entity import DetailL
from .database import db

class DetailLController:
    @staticmethod
    def add_detail_l():
        data = request.json
        detail_l = DetailL(**data)
        db.session.add(detail_l)
        db.session.commit()
        return jsonify(detail_l), 201

    @staticmethod
    def get_all_detail_ls():
        detail_ls = DetailL.query.all()
        return jsonify(detail_ls)

    @staticmethod
    def get_detail_l(id):
        detail_l = DetailL.query.get(id)
        if detail_l:
            return jsonify(detail_l)
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    @staticmethod
    def update_detail_l(id):
        data = request.json
        detail_l = DetailL.query.get(id)
        if detail_l:
            for key, value in data.items():
                setattr(detail_l, key, value)
            db.session.commit()
            return '', 204
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    @staticmethod
    def delete_detail_l(id):
        detail_l = DetailL.query.get(id)
        if detail_l:
            db.session.delete(detail_l)
            db.session.commit()
            return '', 204
        else:
            return jsonify({'message': 'DetailL not found'}), 404

    @staticmethod
    def restore_detail_l(id):
        detail_l = DetailL.query.get(id)
        if detail_l and detail_l.is_deleted:
            detail_l.is_deleted = False
            db.session.commit()
            return jsonify(detail_l)
        else:
            return jsonify({'message': 'Deleted DetailL not found'}), 404

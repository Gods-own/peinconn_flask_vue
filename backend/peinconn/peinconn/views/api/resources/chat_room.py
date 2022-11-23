from flask import request, jsonify, make_response, current_app, url_for
from flask_restful import Resource
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import ActivitySchema, activity_schema, activities_schema
from peinconn.peinconn.models import Activity as UserActivity, Interest, User, Liked, Room
from peinconn.peinconn.helpers.utils import save_file, remove_file, get_file_url
from peinconn.peinconn.helpers.pagination import get_pagination
from peinconn.peinconn.request.activity import activity_request
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user


class CheckChatRoom(Resource):
    @token_required
    def get(self, userId1, userId2):
        try:
            result1 = Room.query.filter_by(user1_id = userId1, user2_id = userId2).first()
            result2 = Room.query.filter_by(user1_id = userId2, user2_id = userId1).first()

            if result1 is None and result2 is None:
                return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Activity Successfully', 'data': False})
            else:
                return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Activity Successfully', 'data': True})    

        except Exception as e:
           return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)

    
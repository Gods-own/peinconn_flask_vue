from flask import request, jsonify, make_response, current_app, url_for
from flask_restful import Resource
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import messages_schema
from peinconn.peinconn.models import Message, Room
from peinconn.peinconn.helpers.pagination import get_pagination, get_pagination_info
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user

class MessageList(Resource):
    @token_required
    def get(self, room_name):
        try:
            auth_user = get_current_user()

            pagination_info = get_pagination_info(request)      

            room = Room.query.filter(Room.room == room_name).first()
            if room is None:
                return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Messages Successfully', 'data': []})

            messages = Message.query.filter(Message.room_id == room.id).order_by(Message.id.desc())

            messages = messages.paginate(page=pagination_info['page'], per_page=pagination_info['per_page'], max_per_page=pagination_info['max_per_page'])        

            messageTransformer = messages_schema.dump(messages)

            links = get_pagination('api.messagelist', messages, room_name=room_name)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Messages Successfully', 'data': messageTransformer, 'links': links})

        except Exception as e:
           return make_response(jsonify({'success': False, 'code': 500, 'message': f'Something went wrong, try again later {e}'}), 500)
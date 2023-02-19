from flask import request, jsonify, make_response, current_app, url_for
from flask_restful import Resource
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import rooms_schema
from peinconn.peinconn.models import Room
from peinconn.peinconn.helpers.pagination import get_pagination, get_pagination_info
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user


class CheckChatRoom(Resource):
    @token_required
    def get(self, userId1, userId2):
        try:
            print('chat')
            result1 = Room.query.filter_by(user1_id = userId1, user2_id = userId2).first()
            result2 = Room.query.filter_by(user1_id = userId2, user2_id = userId1).first()

            if result1 is None and result2 is None:
                return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Room Successfully', 'data': {'status': False, 'room_name':None}})
            else:
                room = Room.query.filter(((Room.user1_id == userId1) & (Room.user2_id == userId2)) | ((Room.user1_id == userId2) & (Room.user2_id == userId1))).first()
                return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Room Successfully', 'data': {'status': True, 'room_name':room.room}})    

        except Exception as e:
           return make_response(jsonify({'success': False, 'code': 500, 'message': f'Something went wrong, try again later {e}'}), 500)

class ChatRoomList(Resource):
    @token_required
    def get(self):
        try:
            print('chat')
            auth_user = get_current_user()

            pagination_info = get_pagination_info(request)

            rooms = Room.query.filter((Room.user1_id == auth_user['id']) | (Room.user2_id == auth_user['id'])).order_by(Room.updated_At.desc())

            rooms = rooms.paginate(page=pagination_info['page'], per_page=pagination_info['per_page'], max_per_page=pagination_info['max_per_page'])        

            roomTransformer = rooms_schema.dump(rooms)

            links = get_pagination('api.chatroomlist', rooms)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Rooms Successfully', 'data': roomTransformer, 'links': links})

        except Exception as e:
           return make_response(jsonify({'success': False, 'code': 500, 'message': f'Something went wrong, try again later {e}'}), 500)



    
from flask import request, jsonify, make_response
from flask_restful import Resource
from peinconn.peinconn.transformers import interests_schema
from peinconn.peinconn.models import Interest, User
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user

class InterestList(Resource):
    def get(self):
        try:
            interests = Interest.query.all();

            interestTransformer = interests_schema.dump(interests)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Interests Successfully', 'data': interestTransformer}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)  

class UserInterestList(Resource):
    @token_required
    def get(self):
        try:
            user = get_current_user()

            user_model = User.query.filter(User.interests.any(User.id==user['id'])).all()

            if len(user_model) == 0: 
                return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Interests Successfully', 'data': []})

            else:
                user_interests = user_model[0].interests

                interestTransformer = interests_schema.dump(user_interests)

                return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Interests Successfully', 'data': interestTransformer}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)  
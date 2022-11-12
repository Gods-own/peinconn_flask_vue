from flask import request, jsonify, make_response
from flask_restful import Resource
from peinconn.peinconn.transformers import interests_schema
from peinconn.peinconn.models import Interest

class InterestList(Resource):
    def get(self):
        try:
            interests = Interest.query.all();

            interestTransformer = interests_schema.dump(interests)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Interests Successfully', 'data': interestTransformer}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)  
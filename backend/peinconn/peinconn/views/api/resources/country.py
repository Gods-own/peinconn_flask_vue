from flask import request, jsonify, make_response
from flask_restful import Resource
from peinconn.peinconn.transformers import countries_schema
from peinconn.peinconn.models import Country

class CountryList(Resource):
    def get(self):

        try:
            countries = Country.query.all();

            countryTransformer = countries_schema.dump(countries)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Countries Successfully', 'data': countryTransformer}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)   
        
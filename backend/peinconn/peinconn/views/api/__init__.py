from flask import Blueprint
from flask_restful import Api, Resource, url_for
from peinconn.peinconn.views.api.resources.activity import ActivityList, Activity, UserActivities
from peinconn.peinconn.views.api.resources.activity_like import LikeActivity
from peinconn.peinconn.views.api.resources.user import User, AllUserDetails
from peinconn.peinconn.views.api.resources.auth import Login, Register
from peinconn.peinconn.views.api.resources.interest_register import RegisterInterest

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(api_bp)

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(User, '/user')
api.add_resource(AllUserDetails, '/all_user_details')
api.add_resource(UserActivities, '/user_activities')
api.add_resource(RegisterInterest, '/interest_registration')
api.add_resource(Activity, '/activities/<activity_id>')
api.add_resource(ActivityList, '/activities')
api.add_resource(LikeActivity, '/activity_like/<activity_id>')


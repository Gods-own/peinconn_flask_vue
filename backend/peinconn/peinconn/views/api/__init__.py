from flask import Blueprint
from flask_restful import Api, Resource, url_for
from peinconn.peinconn.views.api.resources.activity import ActivityList, Activity, UserActivities, ActivityListForUserInterests
from peinconn.peinconn.views.api.resources.country import CountryList
from peinconn.peinconn.views.api.resources.hobby import InterestList, UserInterestList
from peinconn.peinconn.views.api.resources.activity_like import LikeActivity, LikeActivityUser
from peinconn.peinconn.views.api.resources.user import User, AllUserDetails
from peinconn.peinconn.views.api.resources.chat_room import CheckChatRoom, ChatRoomList
from peinconn.peinconn.views.api.resources.chat_message import MessageList
from peinconn.peinconn.views.api.resources.auth import Login, Register
from peinconn.peinconn.views.api.resources.search import Search
from peinconn.peinconn.views.api.resources.interest_register import RegisterInterest

api_bp = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(api_bp)

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(User, '/user/<user_id>')
api.add_resource(AllUserDetails, '/all_user_details/<user_id>')
api.add_resource(CheckChatRoom, '/room/<userId1>/<userId2>')
api.add_resource(ChatRoomList, '/rooms')
api.add_resource(MessageList, '/messages/<room_name>')
api.add_resource(UserActivities, '/user_activities/<user_id>')
api.add_resource(RegisterInterest, '/interest_registration')
api.add_resource(Activity, '/activities/<activity_id>')
api.add_resource(ActivityList, '/activities')
api.add_resource(ActivityListForUserInterests, '/user_interests_activities')
api.add_resource(LikeActivity, '/activity_like/<activity_id>')
api.add_resource(LikeActivityUser, '/activity_likes/<activity_id>')
api.add_resource(CountryList, '/countries')
api.add_resource(Search, '/search')
api.add_resource(InterestList, '/interests')
api.add_resource(UserInterestList, '/user_interests/<user_id>')


from flask import request, jsonify, make_response, current_app, url_for
from flask_restful import Resource
from peinconn.peinconn.extensions import db
from peinconn.peinconn.transformers import ActivitySchema, activity_schema, activities_schema
from peinconn.peinconn.models import Activity as UserActivity, Interest, User, Liked
from peinconn.peinconn.helpers.utils import save_file, remove_file
from peinconn.peinconn.helpers.pagination import get_pagination, get_pagination_info
from peinconn.peinconn.request.activity import activity_request
from peinconn.peinconn.helpers.jwt_auth import token_required, get_current_user


class Activity(Resource):
    @token_required
    def get(self, activity_id):
        try:
            activity = UserActivity.query.filter_by(id = activity_id).one()

            activityTransformer = activity_schema.dump(activity)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Activity Successfully', 'data': activityTransformer}) 
        except Exception as e:
           return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)

    @token_required
    def put(self, activity_id):

        try:
            activity_values_validation = activity_request()

            if activity_values_validation == True:

                activity_model = UserActivity.query.filter_by(id = activity_id).one()

                activity = request.form.get('activity')
                raw_picture = request.files['picture']
                interest_id = request.form.get('interest_id')

                interest = db.session.query(Interest).filter_by(id = interest_id).one()

                file_name = raw_picture.filename
                
                remove_file(activity_model.picture)

                picture = save_file(raw_picture, file_name)

                activity_model.activity = activity
                activity_model.picture = picture
                activity_model.interest = interest

                db.session.commit()

                return make_response(jsonify({'success': True, 'code': 200, 'message': 'Activity Updated Successfully'}), 201)
            else:
                return activity_values_validation     
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)

class ActivityList(Resource):

    @token_required
    def get(self):

        try:

            activities = UserActivity.query.order_by(UserActivity.id.desc())

            # page = request.args.get('page')

            # per_page = request.args.get('per_page')

            # max_per_page =  12

            # if page is not None:
            #     page = int(page)

            # if per_page is None:
            #     per_page = 10
            # else:
            #     if int(per_page) > max_per_page:
            #         per_page = 10   
            #     else:
            #         per_page = int(per_page)     

            pagination_info = get_pagination_info(request)

            activities = activities.paginate(page=pagination_info['page'], per_page=pagination_info['per_page'], max_per_page=pagination_info['max_per_page'])

            activityTransformer = activities_schema.dump(activities)

            links = get_pagination('api.activitylist', activities)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Activity Successfully', 'data': activityTransformer, 'links': links}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': f'Something went wrong, try again later'}), 500) 

    @token_required
    def post(self):

        try:
            activity_values_validation = activity_request()

            if activity_values_validation == True:

                auth_user = get_current_user()

                user = User.query.filter_by(id=auth_user['id']).one()

                activity = request.form.get('activity')
                raw_picture = request.files['picture']
                print(raw_picture)
                interest_id = request.form.get('interest_id')

                interest = db.session.query(Interest).filter_by(id = interest_id).one()

                file_name = raw_picture.filename

                picture = save_file(raw_picture, file_name)

                new_activity = UserActivity(user=user, activity=activity, picture=picture, interest=interest)

                db.session.add(new_activity)
                db.session.commit()

                activityTransformer = activity_schema.dump(new_activity)

                return jsonify({'success': True, 'code': 200, 'message': 'Activity added Successfully', 'data': activityTransformer})
            else:
                return activity_values_validation     
        except Exception as e:
            print(e)
            return make_response(jsonify({'success': False, 'code': 500, 'message': f'Something went wrong, try again later {e}'}), 500)    
        

class UserActivities(Resource):
    @token_required
    def get(self, user_id):

        try:

            interest_filter = request.args.get('filter')

            print(interest_filter)

            if interest_filter is not None:
                user_activities = UserActivity.query.filter_by(user_id=user_id, interest_id=int(interest_filter)).order_by(UserActivity.id.asc())
            else:
                user_activities = UserActivity.query.filter_by(user_id=user_id).order_by(UserActivity.id.asc())

            # page = request.args.get('page')

            # per_page = request.args.get('per_page')

            # max_per_page =  12

            # if page is not None:
            #     page = int(page)

            # if per_page is None:
            #     per_page = 10
            # else:
            #     if per_page > max_per_page:
            #         per_page = 10   
            #     else:
            #         per_page = int(per_page) 

            # user_activities = UserActivity.query.order_by(UserActivity.id.asc())

            pagination_info = get_pagination_info(request)

            user_activities = user_activities.paginate(page=pagination_info['page'], per_page=pagination_info['per_page'], max_per_page=pagination_info['max_per_page'])

            print(user_activities)

            new_activities_schema = ActivitySchema(many=True, exclude=('user',))

            activityTransformer = new_activities_schema.dump(user_activities)

            print(activityTransformer)

            print(pagination_info)

            links = get_pagination('api.useractivities', user_activities, user_id=user_id)

            print(links)

            return jsonify({'success': True, 'code': 200, 'message': 'Activity retrieved Successfully', 'data': activityTransformer, 'links': links})
  
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': 'Something went wrong, try again later'}), 500)   

class ActivityListForUserInterests(Resource):

    @token_required
    def get(self):

        try:
            auth_user = get_current_user()

            interest_filter = request.args.get('filter')

            if interest_filter is not None:
                user_interests_id = [int(interest_filter)]
            else:
                user_model = User.query.filter(User.interests.any(User.id==auth_user['id'])).all()

                if len(user_model) == 0:
                    return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Activity Successfully', 'data': []}) 

                user_interests = user_model[0].interests

                user_interests_id = []

                for user_interest in user_interests:
                    user_interests_id.append(user_interest.id)

            activities = UserActivity.query.filter(UserActivity.interest_id.in_(user_interests_id)).order_by(UserActivity.id.desc())

            # page = request.args.get('page')

            # per_page = request.args.get('per_page')

            # max_per_page =  12

            # if page is not None:
            #     page = int(page)

            # if per_page is None:
            #     per_page = 10
            # else:
            #     if int(per_page) > max_per_page:
            #         per_page = 10   
            #     else:
            #         per_page = int(per_page)     

            pagination_info = get_pagination_info(request)        

            activities = activities.paginate(page=pagination_info['page'], per_page=pagination_info['per_page'], max_per_page=pagination_info['max_per_page'])

            activityTransformer = activities_schema.dump(activities)

            links = get_pagination('api.activitylist', activities)

            return jsonify({'success': True, 'code': 200, 'message': 'Retrieved Activity Successfully', 'data': activityTransformer, 'links': links}) 
        except Exception as e:
            return make_response(jsonify({'success': False, 'code': 500, 'message': f'Something went wrong, try again later'}), 500)               
               
from flask import current_app
from .extensions import ma, db
import os
from peinconn.peinconn.models import Liked
from peinconn.peinconn.helpers.jwt_auth import get_current_user

#Country Schema
class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id', 'country', 'created_At', 'updated_At')  

#Init Country Schema
country_schema = CountrySchema()
countries_schema = CountrySchema(many=True) 

#Interest Schema
class InterestSchema(ma.Schema):
    class Meta:
        fields = ('id', 'hobby', 'hobby_image', 'created_At', 'updated_At')   

#Init Interest Schema
interest_schema = InterestSchema()
interests_schema = InterestSchema(many=True)  

#User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'introduction', 'gender', 'date_of_birth', 'userImage', 'coverImage', 'is_admin', 'is_active', 
        'date_joined', 'last_login', 'interests', 'country', 'created_At', 'updated_At')

    interests = ma.List(ma.Nested(InterestSchema))
    country = ma.Nested(CountrySchema)
    userImage = ma.Method("get_profile_file_url")
    coverImage = ma.Method("get_cover_file_url")

    def get_profile_file_url(self, obj):
        if obj.userImage == "default-image.png":
            url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['DEFAULT_IMAGE_PATH'], obj.userImage)
        else:
            url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['PROFILE_IMAGE_PATH'], obj.userImage)

        file_url = "/".join(url_tupple)

        return file_url
    
    def get_cover_file_url(self, obj):
        if obj.coverImage == "default-cover.jpg":
            url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['DEFAULT_IMAGE_PATH'], obj.coverImage)
        else:
            url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['COVER_IMAGE_PATH'], obj.coverImage)

        file_url = "/".join(url_tupple)

        return file_url

#Init User Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True) 

#Liked Schema
class LikedSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'user', 'activity_id', 'is_liked', 'created_At', 'updated_At')

    user = ma.Nested(UserSchema)
        # activity = ma.Nested("ActivitySchema", exclude=("user",)) 

#Init Liked Schema
liked_schema = LikedSchema()   
likedlist_schema = LikedSchema(many=True) 

#Activity Schema
class ActivitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'activity', 'picture', 'interest', 'is_liked', 'like_no', 'created_At', 'updated_At')    

    user = ma.Nested(UserSchema)
    interest = ma.Nested(InterestSchema)  
    picture = ma.Method("get_file_url")
    is_liked = ma.Method("is_liked_by_user")

    # links = ma.Hyperlinks({
    #         'firstPage':
    #         'lastPage':
    #         'prevPage':
    #         'nextPage':
    #         'meta': {
    #             'paging': {
    #             'paegCount':
    #             'totalPages':
    #             'page':
    #             'hasPrevPage':
    #             'hasNextPage':
    #             }
    #         }
    #     })

    def get_file_url(self, obj):
        url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['ACTIVITY_IMAGE_PATH'], obj.picture )

        print(url_tupple)

        file_url = "/".join(url_tupple)

        return file_url
        
    def is_liked_by_user(self, obj):
        auth_user = get_current_user()
        liked_model = Liked.query.filter_by( user_id = auth_user['id'], activity_id = obj.id, is_liked=True).first()
        if liked_model is None:
            return False
        else:
            return True    

#Init Activity Schema
activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)   

#User Details Schema which includes activities, interests e.t.c
class UserDetailsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'introduction', 'gender', 'date_of_birth', 'userImage', 'coverImage', 'is_admin', 'is_active', 
        'date_joined', 'last_login', 'interests', 'country', 'activities', 'created_At', 'updated_At')

    interests = ma.List(ma.Nested(InterestSchema))
    country = ma.Nested(CountrySchema) 
    activities = ma.List(ma.Nested(ActivitySchema(exclude=("user",))))
    userImage = ma.Method("get_profile_file_url")
    coverImage = ma.Method("get_cover_file_url")

    def get_profile_file_url(self, obj):
        if obj.userImage == "default-image.png":
            url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['DEFAULT_IMAGE_PATH'], obj.userImage)
        else:
            url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['PROFILE_IMAGE_PATH'], obj.userImage)

        file_url = "/".join(url_tupple)

        return file_url
    
    def get_cover_file_url(self, obj):
        if obj.coverImage == "default-cover.jpg":
            url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['DEFAULT_IMAGE_PATH'], obj.coverImage)
        else:
            url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['COVER_IMAGE_PATH'], obj.coverImage)

        file_url = "/".join(url_tupple)

        return file_url

#Init User Schema
user_details_schema = UserDetailsSchema()
users_details_schema = UserDetailsSchema(many=True)   

#Notification Schema
class NotificationSchema(ma.Schema):
    class Meta:
        fields = ('id', 'notification_user_id', 'notification_read', 'created_At', 'updated_At')      

#Init Notification Schema
notification_schema = NotificationSchema() 
notifications_schema = NotificationSchema(many=True)

#Message Schema
class MessageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'sender', 'receiver', 'user1', 'user2', 'new_message', 'content', 'created_At', 'updated_At')

    user1 = ma.Nested(UserSchema(exclude=("interests",)))
    user2 = ma.Nested(UserSchema(exclude=("interests",)))
    new_message = ma.List(ma.Nested(NotificationSchema))      

#Init Message Schema
message_schema = MessageSchema() 
messages_schema = MessageSchema(many=True) 

#Room Schema
class RoomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'room', 'dm_room', 'user1_id', 'user2_id', 'user1', 'user2', 'created_At', 'updated_At')   

    user1 = ma.Nested(UserSchema(exclude=("interests",)))
    user2 = ma.Nested(UserSchema(exclude=("interests",)))  
    dm_room = ma.List(ma.Nested(MessageSchema(exclude=("user1", "user2"))))

#Init Room Schema
room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True) 



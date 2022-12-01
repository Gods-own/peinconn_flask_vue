from flask import current_app
from .extensions import ma
import os

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
        fields = ('id', 'username', 'email', 'introduction', 'gender', 'date_of_birth', 'userImage', 'is_admin', 'is_active', 
        'date_joined', 'last_login', 'interests', 'country', 'created_At', 'updated_At')

    interests = ma.List(ma.Nested(InterestSchema))
    country = ma.Nested(CountrySchema)
    userImage = ma.Method("get_file_url")

    def get_file_url(self, obj):
        url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['PROFILE_IMAGE_PATH'], obj.userImage )
        print(url_tupple)

        file_url = "/".join(url_tupple)

        return file_url

#Init User Schema
user_schema = UserSchema()
users_schema = UserSchema(many=True) 

#Activity Schema
class ActivitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'activity', 'picture', 'interest', 'like_no', 'created_At', 'updated_At')    

    user = ma.Nested(UserSchema)
    interest = ma.Nested(InterestSchema)  
    picture = ma.Method("get_file_url")

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

#Init Activity Schema
activity_schema = ActivitySchema()
activities_schema = ActivitySchema(many=True)   

#User Details Schema which includes activities, interests e.t.c
class UserDetailsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'introduction', 'gender', 'date_of_birth', 'userImage', 'is_admin', 'is_active', 
        'date_joined', 'last_login', 'interests', 'country', 'activities', 'created_At', 'updated_At')

    interests = ma.List(ma.Nested(InterestSchema))
    country = ma.Nested(CountrySchema) 
    activities = ma.List(ma.Nested(ActivitySchema(exclude=("user",))))
    userImage = ma.Method("get_file_url")

    def get_file_url(self, obj):
        url_tupple = (current_app.config['APP_URL'], 'static', current_app.config['PROFILE_IMAGE_PATH'], obj.userImage)

        file_url = "/".join(url_tupple)

        return file_url

#Init User Schema
user_details_schema = UserDetailsSchema()
users_details_schema = UserDetailsSchema(many=True)       

#Liked Schema
class LikedSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'user', 'activity_id', 'activity', 'created_At', 'updated_At')

        user = ma.Nested("UserSchema")
        # activity = ma.Nested("ActivitySchema", exclude=("user",)) 

#Init Liked Schema
liked_schema = LikedSchema()   
likedlist_schema = LikedSchema(many=True) 

#Room Schema
class RoomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'room', 'user1', 'user2', 'created_At', 'updated_At')   

    user1 = ma.Nested(UserSchema(exclude=("interests",)))
    user2 = ma.Nested(UserSchema(exclude=("interests",)))    

#Init Room Schema
room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True) 

#Message Schema
class MessageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'room', 'content', 'created_At', 'updated_At')

    user = ma.Nested(UserSchema)
    room = ma.Nested(RoomSchema(exclude=("user1", "user2",)))        

#Init Message Schema
message_schema = MessageSchema() 
messages_schema = MessageSchema(many=True) 

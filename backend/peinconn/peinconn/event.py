from .extensions import db
from .models import Room, Message, Notifications, Connected
from .transformers import message_schema
from peinconn.peinconn.helpers.jwt_auth import get_current_user, token_required
from flask import request

def save_message(data):
    room = Room.query.filter(((Room.user1_id == data['user1_id']) & (Room.user2_id == data['user2_id'])) | ((Room.user1_id == data['user2_id']) & (Room.user2_id == data['user1_id']))).first()
    print(room)
    if room is None:
        room = Room(room=data['room'], user1_id=data['user1_id'], user2_id=data['user2_id'])
        db.session.add(room)
        db.session.flush()
        db.session.refresh(room)
    print(room.id)
    new_message = Message(user_id=data['user_id'], room_id=room.id, content=data['message'])
    db.session.add(new_message)
    db.session.flush()
    db.session.refresh(new_message)
    notification = Notifications(notification_user_id=data['user2_id'], notification_message_id=new_message.id)
    db.session.add(notification)
    db.session.commit() 
    return new_message

def connect_user(data):
    auth_user = get_current_user()
    # connectedUser = User.objects.get(username=self.scope['user'])
    room = Room.query.filter(Room.room == data['room']).first()
    if Connected.query.filter((Connected.connected_user_id == data['user_id']) & (Connected.connection_room_id == room.id)).first() is None:
        new_connection = Connected(connected_user_id=data['user_id'], connection_room_id=room.id, channel_name=request.sid)
        db.session.add(new_connection)
        db.session.commit()
    if Message.query.filter(Message.room_id==room.id).first() is not None:    
        messagess = Message.query.filter((Message.room_id==room.id) & (Message.user_id!=data['user_id'])).all()
        message_ids = []
        for message in messagess:
            message_ids.append(message.id)
        notification = Notifications.query.filter(Notifications.notification_message_id.in_(message_ids))
        print(str(notification.order_by(Notifications.id.desc()).first().notification_user_id) == str(data['user_id']))
        if str(notification.order_by(Notifications.id.desc()).first().notification_user_id) == str(data['user_id']):
            # notification = Notifications.query.filter(Notifications.notification_message_id.in_(message_ids)).all()
            # print(notification)
            Notifications.query.filter(Notifications.notification_message_id.in_(message_ids)).update({Notifications.notification_read: True})
            db.session.commit()

def disconnect_user(data):
    auth_user = get_current_user()
    room = Room.query.filter(Room.room == data['room']).first()
    if Connected.query.filter((Connected.connected_user_id == data['user_id']) & (Connected.connection_room_id == room.id)).first() is not None:
        connected = Connected.query.filter((Connected.connected_user_id == data['user_id']) & (Connected.connection_room_id == room.id)).first()
        db.session.delete(connected)
        db.session.commit()

def get_connected_users(data):
    room = Room.query.filter(Room.room == data['room'])
    no_of_connected_users = Connected.query.filter(Connected.connection_room_id == room.id).count() 
    return no_of_connected_users

def get_notifications():
    auth_user = get_current_user()
    no_of_notifications = Notifications.query.filter((Notifications.notification_read==False) & (Notifications.notification_user_id==auth_user['id'])).count()
    return no_of_notifications             
from .extensions import db
from .models import Room, Message, User

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
    db.session.commit()  
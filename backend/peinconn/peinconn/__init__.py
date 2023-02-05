from flask import Flask, request, jsonify
from flask_socketio import emit
from .extensions import db, ma, migrate, api, seeder, socketio, cors
from .transformers import message_schema
from .models import Room, Message
from .views.web import web
from .views.api import api_bp
from peinconn import config
from .event import save_message, save_room, connect_user, disconnect_user, get_connected_users, get_notifications
from flask_socketio import join_room, leave_room, send, emit
import json

def create_app():
    app = Flask(__name__)

    app.config.from_object(config.DevelopmentConfig)

    socketio.init_app(app, manage_session=False, cors_allowed_origins="*", engineio_logger=True)
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    seeder.init_app(app, db)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r'/api/v1/*': {'origins':'*'}})

    app.register_blueprint(web) 

    app.register_blueprint(api_bp)

    return app

@socketio.on('connect')
def test_connect(data):
    print('connected')

@socketio.on('userConnected')
def on_connected(data):
    data = json.loads(data)
    room = data['room']
    # join_room(room)
    # new_message = save_message(data)
    # messageTransformer = message_schema.dump(new_message)
    # emit('new_message', messageTransformer, to=room)  
    connect_user(data) 

@socketio.on('join')
def on_join(data):
    data = json.loads(data)
    room = data['room']
    join_room(room)
    # new_message = save_message(data)
    # messageTransformer = message_schema.dump(new_message)
    # emit('new_message', messageTransformer, to=room)  
    save_room(data);
    emit('joined', to=room)   
    connect_user(data)

@socketio.on('message')
def on_message(data):
    data = json.loads(data)
    room = data['room']
    join_room(room)
    new_message = save_message(data)
    messageTransformer = message_schema.dump(new_message)
    emit('new_message', messageTransformer, to=room) 
    emit('notify', messageTransformer, broadcast=True)  
    emit('received')  
    connect_user(data)    

@socketio.on('leave')
def on_leave(data):
    data = json.loads(data) 

@socketio.on('userDisconnected')
def on_disconnected(data):
    data = json.loads(data)
    # room = data['room']
    # join_room(room)
    # new_message = save_message(data)
    # messageTransformer = message_schema.dump(new_message)
    # emit('new_message', messageTransformer, to=room)  
    print('disconnect')
    disconnect_user(data)       


        
   
 




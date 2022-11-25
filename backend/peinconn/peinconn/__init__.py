from flask import Flask, request, jsonify
from flask_socketio import emit
from .extensions import db, ma, migrate, api, seeder, socketio, cors
# from .transformers import ActivitySchema, activity_schema, activities_schema
from .models import Room, Message
from .views.web import web
from .views.api import api_bp
from peinconn import config
from .event import save_message
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
def test_connect():
    print('connected')
    emit('my broadcast', {'data': 'Connected'})    

@socketio.on('join')
def on_join(data):
    data = json.loads(data)
    room = data['room']
    join_room(room)
    print(data)
    save_message(data)


        
   
 




from flask import Flask, request, jsonify
from flask_socketio import emit
from .extensions import db, ma, migrate, api, seeder, socketio, cors
from .views.web import web
from .views.api import api_bp
from peinconn import config

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

@socketio.on('connect', namespace='/login')
def test_connect():
    print('connected')
    emit('my broadcast', {'data': 'Connected'}, namespace='/login')    
   
 




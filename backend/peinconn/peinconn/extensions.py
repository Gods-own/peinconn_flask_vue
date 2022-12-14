from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_seeder import FlaskSeeder
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin

socketio = SocketIO()
db = SQLAlchemy()
seeder = FlaskSeeder()
ma = Marshmallow()
migrate = Migrate()
api = Api()
cors = CORS()
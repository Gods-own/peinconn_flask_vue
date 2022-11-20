from peinconn import app
from .extensions import socketio

if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app)
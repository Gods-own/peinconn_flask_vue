from flask_socketio import emit
from peinconn.peinconn.extensions import socketio

@socketio.on('connect', namespace='/login')
def test_connect():
    print('connected')
    emit('my broadcast', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('disconnected')
    print('Client disconnected')

@socketio.on('my message')
def test_disconnectdd(data):
    print(f'Client disconnected recieved ${data}')
   

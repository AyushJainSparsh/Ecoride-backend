from flask_socketio import join_room, leave_room, emit
from chat.chat_model import save_message
import datetime

# To prevent circular import later
def register_chat_events(socketio):
    @socketio.on('join')
    def handle_join(data):
        room = data['room']
        username = data['username']
        join_room(room)
        emit('system', {'msg': f'{username} joined room {room}'}, room=room)

    @socketio.on('leave')
    def handle_leave(data):
        room = data['room']
        username = data['username']
        leave_room(room)
        emit('system', {'msg': f'{username} left room {room}'}, room=room)

    @socketio.on('message')
    def handle_message(data):
        room = data['room']
        from datetime import datetime

        message = {
            'sender': data['sender'],
            'content': data['content'],
            'room': room,
            'timestamp': datetime.utcnow()
        }

        result = save_message(message)
        message['_id'] = str(result.inserted_id)
        message['timestamp'] = message['timestamp'].isoformat()
        emit('message', message, room=room)


from flask import Blueprint, jsonify
from chat.chat_model import get_messages_by_room

chat_bp = Blueprint('chat_bp', __name__, url_prefix='/api/chat')

@chat_bp.route('/messages/<room>', methods=['GET'])
def get_chat(room):
    messages = get_messages_by_room(room)
    for m in messages:
        m['_id'] = str(m['_id'])
        m['timestamp'] = m['timestamp'].isoformat()
    return jsonify(messages), 200

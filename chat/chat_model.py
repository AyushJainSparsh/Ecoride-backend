from flask import current_app
from datetime import datetime

def get_chat_collection():
    db = current_app.config.get('DB')
    return db.chats

def save_message(message):
    message['timestamp'] = datetime.utcnow()
    return get_chat_collection().insert_one(message)

def get_messages_by_room(room):
    return list(get_chat_collection().find({'room': room}).sort('timestamp', 1))

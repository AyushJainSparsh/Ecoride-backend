from flask import current_app
from datetime import datetime
from bson import ObjectId

def get_notifications_collection():
    db = current_app.config.get('DB')
    return db.notifications

def create_notification(user_id, title, message, data=None):
    notification = {
        'user_id': user_id,
        'title': title,
        'message': message,
        'data': data or {},
        'read': False,
        'created_at': datetime.utcnow()
    }
    return get_notifications_collection().insert_one(notification)

def get_user_notifications(user_id):
    return list(get_notifications_collection().find({'user_id': user_id}).sort('created_at', -1))

def mark_notification_as_read(notification_id):
    return get_notifications_collection().update_one(
        {'_id': ObjectId(notification_id)},
        {'$set': {'read': True}}
    )

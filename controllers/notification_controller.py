from flask import request, jsonify
from models.notification_model import *
from utils.auth import token_required

@token_required
def list_notifications(current_user):
    notifications = get_user_notifications(current_user['_id'])
    for n in notifications:
        n['_id'] = str(n['_id'])
        n['user_id'] = str(n['user_id'])
    return jsonify(notifications), 200

@token_required
def read_notification(current_user, notification_id):
    result = mark_notification_as_read(notification_id)
    if result.modified_count:
        return jsonify({'message': 'Notification marked as read'}), 200
    return jsonify({'error': 'Notification not found'}), 404

from flask import Blueprint
from controllers.notification_controller import *

notification_bp = Blueprint('notification_bp', __name__, url_prefix='/api/notification')

notification_bp.route('/list', methods=['GET'])(list_notifications)
notification_bp.route('/read/<notification_id>', methods=['POST'])(read_notification)

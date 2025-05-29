from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from flask import jsonify, current_app
from bson import ObjectId
from models.user_model import find_user_by_id
from utils.jwt_utils import verify_token

def token_required(f):
    @jwt_required()
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = verify_token()
        user = find_user_by_id(user_id)
      
        if not user:
            return jsonify({'error': 'User not found'}), 401

        user['_id'] = str(user['_id'])
        return f(user, *args, **kwargs)
    return decorated

from functools import wraps
from flask import jsonify

def admin_required(f):
    @wraps(f)
    def decorated(current_user, *args, **kwargs):
        if not current_user.get("is_admin", False):
            return jsonify({"error": "Admin access required"}), 403
        return f(current_user, *args, **kwargs)
    return decorated


from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
from models.user_model import find_user_by_id, update_user_by_id
import cloudinary  # We’ll use Cloudinary for free image hosting
from utils.jwt_utils import verify_token

def get_profile():
    user_id = verify_token()
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({'msg': 'User not found'}), 404
    user['_id'] = str(user['_id'])
    return jsonify(user), 200

def update_profile():
    user_id = verify_token()
    data = request.json
    updated = update_user_by_id(user_id, data)
    if updated:
        return jsonify({'msg': 'Profile updated'}), 200
    return jsonify({'msg': 'Update failed'}), 400

def upload_avatar():
    user_id = verify_token()
    if 'avatar' not in request.files:
        return jsonify({'msg': 'No file uploaded'}), 400

    file = request.files['avatar']
    result = cloudinary.uploader.upload(file.stream)
    avatar_url = result.get("secure_url")

    update_user_by_id(user_id, {'avatar': avatar_url})
    return jsonify({'msg': 'Avatar uploaded', 'avatar': avatar_url}), 200

def update_password():
    user_id = verify_token()
    data = request.json
    old_password = data.get('old_password')
    new_password = data.get('new_password')

    user = find_user_by_id(user_id)
    if not user or not check_password_hash(user['password'], old_password):
        return jsonify({'msg': 'Old password is incorrect'}), 400

    hashed_pw = generate_password_hash(new_password)
    update_user_by_id(user_id, {'password': hashed_pw})
    return jsonify({'msg': 'Password updated successfully'}), 200

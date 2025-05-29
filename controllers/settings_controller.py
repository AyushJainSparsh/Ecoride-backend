from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import get_users_collection
from bson.objectid import ObjectId
import re

def update_password(current_user, data):
    old_password = data.get('old_password')
    new_password = data.get('new_password')
    if not old_password or not new_password:
        return jsonify({'error': 'Old and new passwords required'}), 400

    if not check_password_hash(current_user['password'], old_password):
        return jsonify({'error': 'Old password is incorrect'}), 401

    hashed = generate_password_hash(new_password)
    users_col = get_users_collection()
    users_col.update_one({'_id': ObjectId(current_user['_id'])}, {'$set': {'password': hashed}})
    return jsonify({'message': 'Password updated successfully'}), 200

def update_email(current_user, data):
    new_email = data.get('email')
    if not new_email or not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
        return jsonify({'error': 'Invalid email'}), 400

    users_col = get_users_collection()
    if users_col.find_one({'email': new_email}):
        return jsonify({'error': 'Email already in use'}), 409

    users_col.update_one({'_id': ObjectId(current_user['_id'])}, {'$set': {'email': new_email}})
    return jsonify({'message': 'Email updated successfully'}), 200

def delete_account(current_user):
    users_col = get_users_collection()
    users_col.delete_one({'_id': ObjectId(current_user['_id'])})
    return jsonify({'message': 'Account deleted successfully'}), 200

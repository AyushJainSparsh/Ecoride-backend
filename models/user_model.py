from flask import current_app
from bson import ObjectId

def get_users_collection():
    db = current_app.config.get('DB')
    return db.users

def find_user_by_email(email):
    return get_users_collection().find_one({"email": email})

def create_user(user):
    return get_users_collection().insert_one(user)

def find_user_by_id(user_id):
    return get_users_collection().find_one({"_id": ObjectId(user_id)})  # Ensure you convert user_id to ObjectId

def update_user_by_id(user_id, update_fields):
    result = get_users_collection().update_one({'_id': ObjectId(user_id)}, {'$set': update_fields})
    return result.modified_count > 0
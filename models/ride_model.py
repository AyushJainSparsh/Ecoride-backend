from flask import current_app
from bson import ObjectId
from datetime import datetime

def get_ride_collection():
    db = current_app.config.get('DB')
    return db.rides

def create_ride(ride_data):
    ride_data['created_at'] = datetime.utcnow()
    return get_ride_collection().insert_one(ride_data)

def search_rides(query):
    return list(get_ride_collection().find(query))

def get_ride_by_id(ride_id):
    return get_ride_collection().find_one({'_id': ObjectId(ride_id)})

def get_user_rides(user_id):
    return list(get_ride_collection().find({'$or': [{'driver_id': user_id}, {'passengers': user_id}]}))

def add_join_request(ride_id, user_id):
    return get_ride_collection().update_one(
        {'_id': ObjectId(ride_id)},
        {'$addToSet': {'join_requests': user_id}}
    )

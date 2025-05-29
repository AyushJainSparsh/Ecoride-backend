from flask import jsonify
from models.user_model import get_users_collection
from models.ride_model import get_ride_collection
from bson.objectid import ObjectId

def get_all_users():
    users_col = get_users_collection()
    users = list(users_col.find({}, {"password": 0}))  # hide passwords
    for user in users:
        user["_id"] = str(user["_id"])
    return jsonify(users), 200

def delete_user(user_id):
    users_col = get_users_collection()
    users_col.delete_one({"_id": ObjectId(user_id)})
    return jsonify({"message": "User deleted"}), 200

def get_all_rides():
    rides_col = get_ride_collection()
    rides = list(rides_col.find())
    for ride in rides:
        ride["_id"] = str(ride["_id"])
    return jsonify(rides), 200

def delete_ride(ride_id):
    rides_col = get_ride_collection()
    rides_col.delete_one({"_id": ObjectId(ride_id)})
    return jsonify({"message": "Ride deleted"}), 200

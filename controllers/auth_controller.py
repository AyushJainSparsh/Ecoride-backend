from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from models.user_model import find_user_by_email, create_user , find_user_by_id
from utils.jwt_utils import generate_token, verify_token

def register():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")

    if not email or not password:
        return jsonify({"message": "Missing email or password"}), 400

    if find_user_by_email(email):
        return jsonify({"message": "User already exists"}), 409

    hashed_pw = generate_password_hash(password)
    user = {"email": email, "password": hashed_pw, "name": name}
    result = create_user(user)
    
    token = generate_token(result.inserted_id)
    return jsonify({"token": token}), 201

def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = find_user_by_email(email)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = generate_token(user["_id"])
    return jsonify({"token": token}), 200

def get_current_user():
    user_id = verify_token()
    user = find_user_by_id(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({
        "email": user["email"],
        "name": user["name"],
        "id": str(user["_id"])
    })

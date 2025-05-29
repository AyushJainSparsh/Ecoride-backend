from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.user_controller import get_profile, update_profile, upload_avatar, update_password

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    return get_profile()

@user_bp.route('/profile', methods=['PUT'])
@jwt_required()
def update():
    return update_profile()

@user_bp.route('/avatar', methods=['POST'])
@jwt_required()
def avatar():
    return upload_avatar()

@user_bp.route('/update-password', methods=['PUT'])
@jwt_required()
def change_password():
    return update_password()

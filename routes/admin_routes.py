from flask import Blueprint, request
from controllers.admin_controller import get_all_users, delete_user, get_all_rides, delete_ride
from utils.auth import token_required
from utils.auth import admin_required

admin_bp = Blueprint("admin_bp", __name__, url_prefix="/api/admin")

@admin_bp.route('/users', methods=['GET'])
@token_required
@admin_required
def all_users_route(current_user):
    return get_all_users()

@admin_bp.route('/user/<user_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_user_route(current_user, user_id):
    return delete_user(user_id)

@admin_bp.route('/rides', methods=['GET'])
@token_required
@admin_required
def all_rides_route(current_user):
    return get_all_rides()

@admin_bp.route('/ride/<ride_id>', methods=['DELETE'])
@token_required
@admin_required
def delete_ride_route(current_user, ride_id):
    return delete_ride(ride_id)

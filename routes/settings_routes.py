from flask import Blueprint, request
from utils.auth import token_required
from controllers.settings_controller import update_password, update_email, delete_account

settings_bp = Blueprint("settings_bp", __name__, url_prefix="/api/settings")

@settings_bp.route('/update-password', methods=['PUT'])
@token_required
def update_password_route(current_user):
    return update_password(current_user, request.json)

@settings_bp.route('/update-email', methods=['PUT'])
@token_required
def update_email_route(current_user):
    return update_email(current_user, request.json)

@settings_bp.route('/delete', methods=['DELETE'])
@token_required
def delete_account_route(current_user):
    return delete_account(current_user)

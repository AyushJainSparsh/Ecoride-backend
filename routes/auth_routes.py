from flask import Blueprint
from controllers.auth_controller import register, login, get_current_user
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def signup():
    return register()

@auth_bp.route("/login", methods=["POST"])
def signin():
    return login()

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    return get_current_user()
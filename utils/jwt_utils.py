# utils/jwt_handler.py

from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended.exceptions import NoAuthorizationError

# This replaces jwt.encode
def generate_token(user_id):
    return create_access_token(identity=str(user_id))

# This wraps get_jwt_identity for reuse
def verify_token():
    try:
        user_id = get_jwt_identity()
        return user_id
    except NoAuthorizationError:
        return None

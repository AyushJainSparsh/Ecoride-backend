from flask import Flask , jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os

from config.db import get_db
import config.cloudinary_config

from routes.auth_routes import auth_bp
from routes.user_routes import user_bp
from routes.ride_routes import ride_bp
from routes.notification_routes import notification_bp
from routes.chat_routes import chat_bp
from routes.settings_routes import settings_bp
from routes.admin_routes import admin_bp

from chat.chat_events import register_chat_events

load_dotenv()

app = Flask(__name__)

db = get_db(app)
app.config['DB'] = db

app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))

CORS(app)

jwt = JWTManager(app)
@jwt.unauthorized_loader
def custom_unauthorized(err):
    return jsonify({"msg": "Missing or invalid token"}), 401

socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")
register_chat_events(socketio)

app.route('/')
def index():
    return jsonify({"message": "Welcome to the EcoRide API"}), 200

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(user_bp, url_prefix='/api/user')
app.register_blueprint(ride_bp)
app.register_blueprint(notification_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(admin_bp)



if __name__ == "__main__":
    import eventlet
    import eventlet.wsgi
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)

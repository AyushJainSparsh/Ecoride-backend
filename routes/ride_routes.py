from flask import Blueprint
from controllers.ride_controller import *

ride_bp = Blueprint('ride_bp', __name__, url_prefix='/api/ride')

ride_bp.route('/create', methods=['POST'])(create_ride_route)
ride_bp.route('/search', methods=['GET'])(search_rides_route)
ride_bp.route('/<ride_id>', methods=['GET'])(get_ride_detail)
ride_bp.route('/my-rides', methods=['GET'])(get_my_rides)
ride_bp.route('/join-request/<ride_id>', methods=['PUT'])(request_to_join)

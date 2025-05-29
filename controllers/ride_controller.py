from flask import request, jsonify
from models.ride_model import *
from utils.auth import token_required

@token_required
def create_ride_route(current_user):
    data = request.json
    ride_data = {
        'driver_id': current_user['_id'],
        'source': data.get('source'),
        'destination': data.get('destination'),
        'date': data.get('date'),
        'time': data.get('time'),
        'seats_available': data.get('seats_available'),
        'passengers': [],
        'join_requests': []
    }
    result = create_ride(ride_data)
    return jsonify({'message': 'Ride created', 'ride_id': str(result.inserted_id)}), 201

@token_required
def search_rides_route(current_user):
    source = request.args.get('source')
    destination = request.args.get('destination')
    date = request.args.get('date')

    query = {}
    if source: query['source'] = source
    if destination: query['destination'] = destination
    if date: query['date'] = date

    rides = search_rides(query)
    for r in rides:
        r['_id'] = str(r['_id'])
        r['driver_id'] = str(r['driver_id'])
    return jsonify(rides), 200

@token_required
def get_ride_detail(current_user, ride_id):
    ride = get_ride_by_id(ride_id)
    if not ride:
        return jsonify({'error': 'Ride not found'}), 404
    ride['_id'] = str(ride['_id'])
    ride['driver_id'] = str(ride['driver_id'])
    return jsonify(ride), 200

@token_required
def get_my_rides(current_user):
    rides = get_user_rides(current_user['_id'])
    for ride in rides:
        ride['_id'] = str(ride['_id'])
        ride['driver_id'] = str(ride['driver_id'])
    return jsonify(rides), 200

@token_required
def request_to_join(current_user, ride_id):
    result = add_join_request(ride_id, current_user['_id'])
    if result.modified_count:
        return jsonify({'message': 'Join request sent'}), 200
    return jsonify({'error': 'Failed to send request'}), 400

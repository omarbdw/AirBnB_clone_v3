#!/usr/bin/python3
""" Handles Places API """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.place import Place


@app_views.route('/cities/<city_id>/places/', methods=['GET'])
def list_places_of_city(city_id):
    '''Retrieves a list of all Place objects in city'''
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    places = city.places
    places_list = []
    for place in places:
        places_list.append(place.to_dict())
    return jsonify(places_list)


@app_views.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    '''Retrieves the list of all Place objects of
    a City: GET /api/v1/cities/<city_id>/places
    If the city_id is not linked to any City
    object, raise a 404 error
    '''
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    '''Deletes a Place object'''
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places/', methods=['POST'])
def post_place(city_id):
    '''Creates a Place object'''
    city = storage.get('City', city_id)
    if city is None:
        abort(404)
    if not request.json:
        abort(400, 'Not a JSON')
    if 'user_id' not in request.json:
        abort(400, 'Missing user_id')
    if 'name' not in request.json:
        abort(400, 'Missing name')
    new_place = Place(**request.json)
    new_place.city_id = city_id
    new_place.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'])
def put_place(place_id):
    '''Updates a Place object'''
    place = storage.get('Place', place_id)
    if place is None:
        abort(404)
    for key, value in request.json.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict())


@app_views.route('/places_search', methods=['POST'])
def search_places():
    '''Searches for Place objects'''
    if not request.json:
        abort(400, 'Not a JSON')
    places = storage.all('Place').values()
    places_list = []
    for place in places:
        places_list.append(place.to_dict())
    return jsonify(places_list)

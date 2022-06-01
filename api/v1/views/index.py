#!/usr/bin/python3
"""index.py to connect to API"""
from api.v1.views import app_views, jsonify
from models import storage
classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def status():
    """Status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def Stats():
    """Stats"""
    dict = {}
    for key, value in classes.items():
        dict[key] = storage.count(value)
    return jsonify(dict)

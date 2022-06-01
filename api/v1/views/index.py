#!/usr/bin/python3
"""index.py to connect to API"""
from api.v1.views import app_views, jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """hbnbStatus"""
    return jsonify({"status": "OK"})

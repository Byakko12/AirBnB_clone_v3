#!/usr/bin/python3
"""app.py to connect to API"""
from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response

HBNB_API_HOST = getenv('HBNB_API_HOST')
HBNB_API_PORT = getenv('HBNB_API_PORT')

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(code):
    """teardown_appcontext"""
    storage.close()


@app.errorhandler(404)
def error_404(self):
    """ handle error_404 """
    error_dict = {"error": "Not found"}
    return make_response(jsonify(error_dict), 404)


def port_host(HBNB_API_HOST, HBNB_API_PORT):
    """set up host and port variables"""
    if not HBNB_API_HOST:
        HBNB_API_HOST = '0.0.0.0'
    if not HBNB_API_PORT:
        HBNB_API_PORT = '5000'


if __name__ == "__main__":
    port_host(HBNB_API_HOST, HBNB_API_PORT)
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, debug=True, threaded=True)

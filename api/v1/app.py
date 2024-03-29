#!/usr/bin/python3
"""
This is the main file for the AirBnB clone v3 API.
"""
from flask import Flask, jsonify, make_response
from api.v1.views import app_views
from models import storage
from os import getenv
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)



@app.teardown_appcontext
def teardown_appcontext(exception):
    """
    Closes the storage connection at the end of the request.
    """
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles 404 errors.
    """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    if getenv("HBNB_API_HOST") is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = getenv("HBNB_API_HOST")
    if getenv("HBNB_API_PORT") is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(getenv("HBNB_API_PORT"))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)

#!/usr/bin/python3
""" This module creates a Blueprint object app_views that handles all views"""
from flask import Flask, jsonify

app = Flask(__name__)


@app_views.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "OK"})


if __name__ == '__main__':
    app.run()

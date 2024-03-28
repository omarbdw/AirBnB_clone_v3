#!/usr/bin/python3
""" This module creates a Blueprint object app_views that handles all views"""
from flask import Blueprint
if app_views is not None:
    from api.v1.views.index import *
    
    
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
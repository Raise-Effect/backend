from flask import Blueprint, jsonify
from flask import current_app as app

api = Blueprint('api', __name__, url_prefix='/')

@api.route('/', methods=['GET'])
def index():
    return 'Hello world'

@api.route('county', methods=['GET'])
def county_data():
    data = {
        "population": 1000,
        "adults": 350,
        "children": 650,
        "laborforce": 900,
        "employed": 800,
        "unemployed": 100
    }
    return jsonify(data)

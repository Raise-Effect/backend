from flask import Blueprint, jsonify
from flask import current_app as app

api = Blueprint('api', __name__, url_prefix='/api/v1/')

@api.route('/', methods=['GET'])
def index():
    return """Hello. Sourcecode and docs for this API available
            <a href=https://github.com/Jobs-Economy/backend>here</a>"""

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

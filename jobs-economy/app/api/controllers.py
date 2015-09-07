from flask import Blueprint, jsonify, make_response
from flask import current_app as app, request
from . import models, query

api = Blueprint('api', __name__, url_prefix='/api/v1/')

@api.route('/', methods=['GET'])
def index():
    return """Hello. Sourcecode and docs for this API available
            <a href=https://github.com/Jobs-Economy/backend>here</a>"""

@api.route('counties/<int:fips>', methods=['GET'])
def counties(fips):
    return jsonify({
        'href': request.path,
        'name': models.County.query.get(fips).county,
        'fips': fips
        })

@api.route('counties/labor-stats', methods=['GET'])
def labor_stats_all():
    return query.construct_labor_stats_all()

@api.route('county/<int:fips>/labor-stats', methods=['GET'])
def labor_stats_for_county(fips):
    return query.construct_labor_stats_for_county(fips)

@api.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': 'Not found: ' + request.url
    }
    resp = jsonify(message)
    return make_response(resp, 404)

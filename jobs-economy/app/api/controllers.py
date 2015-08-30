from flask import Blueprint, jsonify
from flask import current_app as app, request
import models

api = Blueprint('api', __name__, url_prefix='/api/v1/')

@api.route('/', methods=['GET'])
def index():
    return """Hello. Sourcecode and docs for this API available
            <a href=https://github.com/Jobs-Economy/backend>here</a>"""

@api.route('counties/<int:fips>', methods=['GET'])
def counties(fips):
    return jsonify({
        'href': request.path,
        'name': models.County.query.filter_by(fips = fips).first().county,
        'fips': fips
        })

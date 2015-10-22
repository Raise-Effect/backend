from flask import Blueprint, jsonify, make_response
from flask import request, current_app
from . import query
from datetime import timedelta
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, (str, bytes)):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, (str, bytes)):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

api = Blueprint('api', __name__, url_prefix='/api/v1/')


@api.route('/', methods=['GET'])
@crossdomain(origin='*')
def index():
    return """Hello. Sourcecode and docs for this API available
    <a href="https://github.com/Jobs-Economy/backend">here</a>"""


@api.route('counties', methods=['GET'])
@crossdomain(origin='*')
def counties_all():
    return query.construct_counties()


@api.route('counties/<int:fips>', methods=['GET'])
@crossdomain(origin='*')
def county(fips):
    return query.construct_county(fips)


@api.route('counties/laborstats', methods=['GET'])
@crossdomain(origin='*')
def laborstats_all():
    return query.construct_laborstats_all()


@api.route('counties/<int:fips>/laborstats', methods=['GET'])
@crossdomain(origin='*')
def laborstats_for_county(fips):
    return query.construct_laborstats_for_county(fips)


@api.route('counties/populations', methods=['GET'])
@crossdomain(origin='*')
def populations_all():
    return query.construct_populations_all()


@api.route('counties/<int:fips>/populations', methods=['GET'])
@crossdomain(origin='*')
def populations_for_county(fips):
    return query.construct_populations_for_county(fips)


@api.route('counties/familytypes', methods=['GET'])
@crossdomain(origin='*')
def familytypes_all():
    return query.construct_familytypes_all()


@api.route('counties/wagestats', methods=['GET'])
@crossdomain(origin='*')
def wagestats_all():
    return query.construct_wagestats_all()


@api.route('counties/<int:fips>/wagestats', defaults={'year': 2013}, methods=['GET'])
@api.route('counties/<int:fips>/wagestats/<int:year>', methods=['GET'])
@crossdomain(origin='*')
def wagestats_for_county(fips, year):
    return query.construct_wagestats_for_county(fips, year)


@api.route('counties/calculatedstats', methods=['GET'])
@crossdomain(origin='*')
def calculatedstats_all():
    return query.construct_calculatedstats_all()


@api.route('counties/<int:fips>/calculatedstats', methods=['GET'])
@crossdomain(origin='*')
def calculatedstats_for_county(fips):
    return query.construct_calculatedstats_for_county(fips)


@api.route('counties/sssbudgets', methods=['GET'])
@crossdomain(origin='*')
def sssbudgets_all():
    return query.construct_sssbudgets_all()


@api.route('counties/<int:fips>/sssbudgets', methods=['GET'])
@crossdomain(origin='*')
def sssbudgets_for_county(fips):
    return query.construct_sssbudgets_for_county(fips)


@api.route('counties/ssscredits', methods=['GET'])
@crossdomain(origin='*')
def ssscredits_all():
    return query.construct_ssscredits_all()


@api.route('counties/<int:fips>/ssscredits', methods=['GET'])
@crossdomain(origin='*')
def ssscredits_for_county(fips):
    return query.construct_ssscredits_for_county(fips)


@api.route('counties/ssswages', methods=['GET'])
@crossdomain(origin='*')
def ssswages_all():
    return query.construct_ssswages_all()


@api.route('counties/<int:fips>/ssswages', methods=['GET'])
@crossdomain(origin='*')
def ssswages_for_county(fips):
    return query.construct_ssswages_for_county(fips)


@api.route('counties/pumas', methods=['GET'])
@crossdomain(origin='*')
def pumas_all():
    return query.construct_pumas_all()


@api.route('counties/<int:fips>/pumas', methods=['GET'])
@crossdomain(origin='*')
def pumas_for_county(fips):
    return query.construct_pumas_for_county(fips)


@api.route('counties/censushouseholds', methods=['GET'])
@crossdomain(origin='*')
def censushouseholds_all():
    return query.construct_censushouseholds_all()


@api.route('counties/<int:fips>/censushouseholds', methods=['GET'])
@crossdomain(origin='*')
def censushouseholds_for_county(fips):
    return query.construct_censushouseholds_for_county(fips)


@api.route('counties/familycodeweights', methods=['GET'])
@crossdomain(origin='*')
def familycodeweights_all():
    return query.construct_familycodeweights_all()


@api.route('counties/<int:fips>/familycodeweights', methods=['GET'])
@crossdomain(origin='*')
def familycodeweights_for_county(fips):
    return query.construct_familycodeweights_for_county(fips)


@api.errorhandler(404)
@crossdomain(origin='*')
def not_found(error):
    message = {
        'status': 404,
        'errorMessage': 'Not found: ' + request.url
    }
    resp = jsonify(message)
    return make_response(resp, 404)

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


@api.route('counties/population', methods=['GET'])
@crossdomain(origin='*')
def population_all():
    return query.construct_population_all()


@api.route('counties/<int:fips>/population', methods=['GET'])
@crossdomain(origin='*')
def population_for_county(fips):
    return query.construct_population_for_county(fips)


@api.route('counties/familytype', methods=['GET'])
@crossdomain(origin='*')
def familytype_all():
    return query.construct_familytype_all()


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


@api.route('counties/sssbudget', methods=['GET'])
@crossdomain(origin='*')
def sssbudget_all():
    return query.construct_sssbudget_all()


@api.route('counties/<int:fips>/sssbudget', methods=['GET'])
@crossdomain(origin='*')
def sssbudget_for_county(fips):
    return query.construct_sssbudget_for_county(fips)


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


@api.route('counties/puma', methods=['GET'])
@crossdomain(origin='*')
def puma_all():
    return query.construct_puma_all()


@api.route('counties/<int:fips>/puma', methods=['GET'])
@crossdomain(origin='*')
def puma_for_county(fips):
    return query.construct_puma_for_county(fips)


@api.route('counties/censushousehold', methods=['GET'])
@crossdomain(origin='*')
def censushousehold_all():
    return query.construct_censushousehold_all()


@api.route('counties/<int:fips>/censushousehold', methods=['GET'])
@crossdomain(origin='*')
def censushousehold_for_county(fips):
    return query.construct_censushousehold_for_county(fips)


@api.errorhandler(404)
@crossdomain(origin='*')
def not_found(error):
    message = {
        'status': 404,
        'errorMessage': 'Not found: ' + request.url
    }
    resp = jsonify(message)
    return make_response(resp, 404)

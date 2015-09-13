from flask import Blueprint, jsonify, make_response, render_template
from flask import request
from . import models, query

api = Blueprint('api', __name__, url_prefix='/api/v1/')


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('counties/<int:fips>', methods=['GET'])
def counties(fips):
    return jsonify({
        'href': request.path,
        'name': models.County.query.get(fips).county,
        'fips': fips
        })


@api.route('counties/laborstats', methods=['GET'])
def laborstats_all():
    return query.construct_laborstats_all()


@api.route('county/<int:fips>/laborstats', methods=['GET'])
def laborstats_for_county(fips):
    return query.construct_laborstats_for_county(fips)


@api.route('counties/population', methods=['GET'])
def population_all():
    return query.construct_population_all()


@api.route('counties/<int:fips>/population', methods=['GET'])
def population_for_county(fips):
    return query.construct_population_for_county(fips)


@api.route('counties/familytype', methods=['GET'])
def familytype_all():
    return query.construct_familytype_all()


@api.route('counties/<int:fips>/familytype', methods=['GET'])
def familytype_for_county(fips):
    return query.construct_familytype_for_county(fips)


@api.route('counties/wagestats', methods=['GET'])
def wagestats_all():
    return query.construct_wagestats_all()


@api.route('counties/<int:fips>/wagestats', defaults={'year': 2013}, methods=['GET'])
@api.route('counties/<int:fips>/wagestats/<int:year>', methods=['GET'])
def wagestats_for_county(fips, year):
    return query.construct_wagestats_for_county(fips, year)


@api.route('counties/calculatedstats', methods=['GET'])
def calcalatedstats_all():
    return query.construct_calculatedstats_all()


@api.route('counties/<int:fips>/calculatedstats', methods=['GET'])
def calculatedstats_for_county(fips):
    return query.construct_calculatedstats_for_county(fips)


@api.route('counties/sssbudget', methods=['GET'])
def sssbudget_all():
    return query.construct_sssbudget_all()


@api.route('counties/<int:fips>/sssbudget', methods=['GET'])
def sssbudget_for_county(fips):
    return query.construct_sssbudget_for_county(fips)


@api.route('counties/ssscredits', methods=['GET'])
def ssscredits_all():
    return query.construct_ssscredits_all()


@api.route('counties/<int:fips>/ssscredits', methods=['GET'])
def ssscredits_for_county():
    return query.construct_ssscredits_for_county()


@api.route('counties/ssswages', methods=['GET'])
def ssswages_all():
    return query.construct_ssswages_all()


@api.route('counties/<int:fips>/ssswages', methods=['GET'])
def ssswages_for_county():
    return query.construct_ssswages_for_county()


@api.route('counties/puma', methods=['GET'])
def puma_all():
    return query.construct_puma_all()


@api.route('counties/<int:fips>/puma', methods=['GET'])
def puma_for_county():
    return query.construct_puma_for_county()


@api.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'errorMessage': 'Not found: ' + request.url
    }
    resp = jsonify(message)
    return make_response(resp, 404)

from functools import lru_cache
from . import models, controllers


def lru_jsonify_cache(**kwargs):
    # TODO: Implemementation broken
    raise NotImplemented
    @lru_cache(**kwargs)
    def f(*params, **kwargs):
        return jsonify()
    return lru_cache(**kwargs)(f)


@lru_jsonify_cache()
def construct_county(fips, expand_fields):
    county = models.County.query.get(fips)

def construct_labor_stats_all():
    data = [
      {
        "fips": stat.fips,
        "laborForce": stat.laborforce,
        "employed": stat.employed,
        "unemployed": stat.unemployed,
        "unemploymentRate": stat.unemploymentrate,
        "urSeasonalAdj": stat.urseasonaladj,
        "year": stat.year
    }
      for stat in models.LaborStats.query]
    return jsonify(data=data)

def construct_labor_stats_for_county(fips):
    stat = models.LaborStats.query.get(fips)
    if stat is not None:
        return jsonify({
          "fips": stat.fips,
          "laborForce": stat.laborforce,
          "employed": stat.employed,
          "unemployed": stat.unemployed,
          "unemploymentRate": stat.unemploymentrate,
          "urSeasonalAdj": stat.urseasonaladj,
          "year": stat.year
        })
    else:
        return controllers.not_found()

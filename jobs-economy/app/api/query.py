from functools import lru_cache, wraps
from . import models
from flask import jsonify


LRU_CACHES = []


def jsonify_lru_cache(**kwargs):
    """
    Cache database query results using functools.lru_cache and convert the
    function return value to response with the json:

    {
        "data": <return value>
    }

    The cache object is available at function_object.__wrapped__. See also:

    https://docs.python.org/3/library/functools.html#functools.lru_cache
    """

    def decorate(f):
        cache_wrapper = lru_cache(**kwargs)(f)
        LRU_CACHES.append(cache_wrapper)

        @wraps(cache_wrapper)
        def jsonify_wrapper(*params, **kwargs):
            return jsonify(data=cache_wrapper(*params, **kwargs))
        return jsonify_wrapper
    return decorate


def clear_caches():
    for cache in LRU_CACHES:
        cache.clear_cache()


@jsonify_lru_cache()
def construct_county(fips):
    return {
        'laborStats': construct_laborstats_for_county(fips),
        'population': construct_population_for_county(fips),
        'familyType': construct_familytype_for_county(fips),
        'wageStats': construct_wagestats_for_county(fips),
        'calculatedStats': construct_calculatedstats_for_county(fips),
        'sssBudget': construct_sssbudget_for_county(fips),
        'sssCredits': construct_ssscredits_for_county(fips),
        'sssWages': construct_ssswages_for_county(fips),
    }


@jsonify_lru_cache()
def construct_counties():
    data = [{
        'fips': county.fips,
        'name': county.county,
    } for county in models.County.query]
    return data


@jsonify_lru_cache()
def construct_laborstats_all():
    data = [{
        "fips": stat.fips,
        "laborForce": stat.laborforce,
        "employed": stat.employed,
        "unemployed": stat.unemployed,
        "unemploymentRate": stat.unemploymentrate,
        "urSeasonalAdj": stat.urseasonaladj,
        "year": stat.year
    } for stat in models.LaborStats.query]
    return data


@jsonify_lru_cache()
def construct_laborstats_for_county(fips):
    stat = models.LaborStats.query.filter_by(fips=fips).first_or_404()
    return {
        "fips": stat.fips,
        "laborForce": stat.laborforce,
        "employed": stat.employed,
        "unemployed": stat.unemployed,
        "unemploymentRate": stat.unemploymentrate,
        "urSeasonalAdj": stat.urseasonaladj,
        "year": stat.year
    }


@jsonify_lru_cache()
def construct_population_all():
    return [
        {
              "fips": stat.fips,
              "population": stat.population,
              "adults": stat.adults,
              "kids": stat.kids,
              "kidspresentc": stat.kidspresentc,
              "a1cC": stat.a1cc,
              "a2s2C": stat.a2s2c,
              "a1c0C": stat.a1c0c,
              "a1teenC": stat.a1teenc,
              "mindiff": stat.mindiff,
              "mostcommonfamilytype": stat.mostcommonfamilytype,
              "year": stat.year
        } for stat in models.Population.query]


@jsonify_lru_cache()
def construct_population_for_county(fips):
    stat = models.Population.query.filter_by(fips=fips).first_or_404()
    return {
          "fips": stat.fips,
          "population": stat.population,
          "adults": stat.adults,
          "kids": stat.kids,
          "kidspresentc": stat.kidspresentc,
          "a1cC": stat.a1cc,
          "a2s2C": stat.a2s2c,
          "a1c0C": stat.a1c0c,
          "a1teenC": stat.a1teenc,
          "mindiff": stat.mindiff,
          "mostcommonfamilytype": stat.mostcommonfamilytype,
          "year": stat.year
    }


@jsonify_lru_cache()
def construct_familytype_all():
    return [
        {
            "familycode": stat.familycode,
            "description-fc": stat.descriptionfc,
            "familycode-rollup": stat.familycoderollup,
            "description-fcr": stat.descriptionfcr,
            "adults": stat.adults,
            "infants": stat.infants,
            "preschoolers": stat.preschoolers,
            "schoolage": stat.schoolage,
            "teenagers": stat.teenagers,
            "children": stat.children
        } for stat in models.FamilyType.query]


@jsonify_lru_cache()
def construct_familytype_for_county(fips):
    stat = models.FamilyType.query.filter_by(fips=fips).first_or_404()
    return {
        "familycode": stat.familycode,
        "description-fc": stat.descriptionfc,
        "familycode-rollup": stat.familycoderollup,
        "description-fcr": stat.descriptionfcr,
        "adults": stat.adults,
        "infants": stat.infants,
        "preschoolers": stat.preschoolers,
        "schoolage": stat.schoolage,
        "teenagers": stat.teenagers,
        "children": stat.children
    }


@jsonify_lru_cache()
def construct_wagestats_all():
    return [
        {
            "fips": stat.fips,
            "medianwage": stat.medianwage,
            "medianhourly": stat.medianhourly,
            "lessthan10hour": stat.lessthan10hour,
            "btwn10and15hour": stat.btwn10and15hour,
            "totalunder15": stat.totalunder15,
            "totalpercentorjobs": stat.totalpercentorjobs,
            "countysalary": stat.countysalary,
            "countywage": stat.countywage,
            "countywageh2": stat.countywageh2,
            "countywagerank": stat.countywagerank,
            "countywageh2rank": stat.countywageh2rank,
            "year": stat.year
        } for stat in models.WageStats.query]


@jsonify_lru_cache()
def construct_wagestats_for_county(fips, year=2013):
    stat = models.WageStats.query.filter_by(fips=fips).first_or_404()
    return {
        "fips": stat.fips,
        "medianwage": stat.medianwage,
        "medianhourly": stat.medianhourly,
        "lessthan10hour": stat.lessthan10hour,
        "btwn10and15hour": stat.btwn10and15hour,
        "totalunder15": stat.totalunder15,
        "totalpercentorjobs": stat.totalpercentorjobs,
        "countysalary": stat.countysalary,
        "countywage": stat.countywage,
        "countywageh2": stat.countywageh2,
        "countywagerank": stat.countywagerank,
        "countywageh2rank": stat.countywageh2rank,
        "year": year
    }


@jsonify_lru_cache()
def construct_calculatedstats_all():
    return [
        {
            "fips": stat.fips,
            "percentorkids": stat.percentorkids,
            "a1allper": stat.a1allper,
            "a2allper": stat.a2allper,
            "c0allper": stat.c0allper
        } for stat in models.CalculatedStats.query]


@jsonify_lru_cache()
def construct_calculatedstats_for_county(fips):
    stat = models.CalculatedStats.query.filter_by(fips=fips).first_or_404()
    return {
        "fips": stat.fips,
        "percentorkids": stat.percentorkids,
        "a1allper": stat.a1allper,
        "a2allper": stat.a2allper,
        "c0allper": stat.c0allper
    }


@jsonify_lru_cache()
def construct_sssbudget_all():
    return [
        {
            "sssbudgetid": stat.sssbudgetid,
            "familycode": stat.familycode,
            "fips": stat.fips,
            "housing": stat.housing,
            "childcare": stat.childcare,
            "food": stat.food,
            "transportation": stat.transportation,
            "healthcare": stat.healthcare,
            "miscellaneous": stat.miscellaneous,
            "taxes": stat.taxes,
            "year": stat.year
        } for stat in models.SssBudget.query]


@jsonify_lru_cache()
def construct_sssbudget_for_county(fips):
    stat = models.SssBudget.query.filter_by(fips=fips).first_or_404()
    return {
        "sssbudgetid": stat.sssbudgetid,
        "familycode": stat.familycode,
        "housing": stat.housing,
        "childcare": stat.childcare,
        "food": stat.food,
        "transportation": stat.transportation,
        "healthcare": stat.healthcare,
        "miscellaneous": stat.miscellaneous,
        "taxes": stat.taxes,
        "fips": stat.fips,
        "year": stat.year
    }


@jsonify_lru_cache()
def construct_ssscredits_all():
    return [
        {
            "ssscreditsid": stat.ssscreditsid,
            "familycode": stat.familycode,
            "oregonworkingfamilycredit": stat.oregonworkingfamilycredit,
            "earnedincometax": stat.earnedincometax,
            "childcaretax": stat.childcaretax,
            "childtax": stat.childtax,
            "fips": stat.fips,
            "year": stat.year
        } for stat in models.SssCredits.query]


@jsonify_lru_cache()
def construct_ssscredits_for_county(fips):
    stat = models.SssCredits.query.filter_by(fips=fips).first_or_404()
    return {
        "ssscreditsid": stat.ssscreditsid,
        "familycode": stat.familycode,
        "oregonworkingfamilycredit": stat.oregonworkingfamilycredit,
        "earnedincometax": stat.earnedincometax,
        "childcaretax": stat.childcaretax,
        "childtax": stat.childtax,
        "fips": stat.fips,
        "year": stat.year
    }


@jsonify_lru_cache()
def construct_ssswages_all():
    return [
        {
            "ssswagesid": stat.ssswagesid,
            "familycode": stat.familycode,
            "hourly": stat.hourly,
            "qualifier": stat.qualifier,
            "monthly": stat.monthly,
            "annual": stat.annual,
            "fips": stat.fips,
            "year": stat.year
        } for stat in models.SssWages.query]


@jsonify_lru_cache()
def construct_ssswages_for_county(fips):
    stat = models.SssWages.query.filter_by(fips=fips).first_or_404()
    return {
        "ssswagesid": stat.ssswagesid,
        "familycode": stat.familycode,
        "hourly": stat.hourly,
        "qualifier": stat.qualifier,
        "monthly": stat.monthly,
        "annual": stat.annual,
        "fips": stat.fips,
        "year": stat.year
    }


@jsonify_lru_cache()
def construct_puma_all():
    return [
        {
            "pumafipsid": stat.pumafipsid,
            "fips": stat.fips,
            "pumacode": stat.pumacode,
            "areaname": stat.areaname,
            "pumaname": stat.pumaname,
            "pumapopulation": stat.pumapopulation,
            "pumaweight": stat.pumaweight
        }
        for stat in models.Puma.query]


@jsonify_lru_cache()
def construct_puma_for_county(fips):
    stat = models.Puma.query.filter_by(fips=fips).first_or_404()
    return {
        "pumafipsid": stat.pumafipsid,
        "fips": stat.fips,
        "pumacode": stat.pumacode,
        "areaname": stat.areaname,
        "pumaname": stat.pumaname,
        "pumapopulation": stat.pumapopulation,
        "pumaweight": stat.pumaweight
    }

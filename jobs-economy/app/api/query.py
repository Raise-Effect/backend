from functools import lru_cache, wraps
from . import models


def jsonify_lru_cache(**kwargs):
    """
    Cache database query results using functools.lru_cache and convert the
    function return value to response with the json:

    {
        "data": <return value>
    }

    See also:
    https://docs.python.org/3/library/functools.html#functools.lru_cache
    """
    def decorate(f):
        cache_wrapper = lru_cache(**kwargs)(f)
        @wraps(cache_wrapper)
        def jsonify_wrapper(*params, **kwargs):
            return jsonify(data=cache_wrapper(*params, **kwargs))
        return jsonify_wrapper
    return decorate


@jsonify_lru_cache()
def construct_county(fips, expand_fields):
    county = models.County.query.get(fips)


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


@jsonify_lru_cache
def construct_laborstats_for_county(fips):
    stat = models.LaborStats.query.get_or_404(fips)
    return {
        "fips": stat.fips,
        "laborForce": stat.laborforce,
        "employed": stat.employed,
        "unemployed": stat.unemployed,
        "unemploymentRate": stat.unemploymentrate,
        "urSeasonalAdj": stat.urseasonaladj,
        "year": stat.year
    }


@jsonify_lru_cache
def construct_population_all():
    return [
        {
              "fips": stat.fips,
              "population": stat.population,
              "adults": stat.adults,
              "kids": stat.kids,
              "kidspresentc": stat.kidspresentc,
              "a1cC": stat.a1cC,
              "a2s2C": stat.a2s2C,
              "a1c0C": stat.a2c0C,
              "a1teenC": stat.a1teenC,
              "mindiff": stat.mindiff,
              "mostcommonfamilytype": stat.mostcommonfamilytype,
              "year": stat.year
        }
    for stat in models.Population.query]


@jsonify_lru_cache
def construct_population_for_county(fips):
    stat = models.Population.query.get_or_404(fips)
    return {
          "fips": stat.fips,
          "population": stat.population,
          "adults": stat.adults,
          "kids": stat.kids,
          "kidspresentc": stat.kidspresentc,
          "a1cC": stat.a1cC,
          "a2s2C": stat.a2s2C,
          "a1c0C": stat.a2c0C,
          "a1teenC": stat.a1teenC,
          "mindiff": stat.mindiff,
          "mostcommonfamilytype": stat.mostcommonfamilytype,
          "year": stat.year
    }


@jsonify_lru_cache
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
        }
    for stat in models.FamilyType.query]


@jsonify_lru_cache
def construct_familytype_for_county(fips):
    stat = models.FamilyType.query.get_or_404(fips)
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


@jsonify_lru_cache
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
        }
    for stat in models.WageStats.query]


@jsonify_lru_cache
def construct_wagestats_for_county(fips):
    stat = models.WageStats.query.get_or_404(fips)
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
        "year": stat.year
    }


@jsonify_lru_cache
def construct_calculatedstats_all():
    return [
        {
            "fips": stat.fips,
            "percentorkids": stat.percentorkids,
            "a1allper": stat.a1allper,
            "a2allper": stat.a2allper,
            "c0allper": stat.c0allper
        }
    for stat in models.CalculatedStats.query]


@jsonify_lru_cache
def construct_calculatedstats_for_county(fips):
    stat = models.CalculatedStats.query.get_or_404(fips)
    return {
        "fips": stat.fips,
        "percentorkids": stat.percentorkids,
        "a1allper": stat.a1allper,
        "a2allper": stat.a2allper,
        "c0allper": stat.c0allper
    }


@jsonify_lru_cache
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
        }
    for stat in models.SssBudget.query]


@jsonify_lru_cache
def construct_sssbudget_for_county(fips):
    stat = models.SssBudget.query.get_or_404(fips)
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


@jsonify_lru_cache
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
        }
    for stat in models.SssCredits.query]


@jsonify_lru_cache
def construct_ssscredits_for_county(fips):
    stat = models.SssCredits.query.get_or_404(fips)
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


@jsonify_lru_cache
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
        }
    for stat in models.SssWages.query]


@jsonify_lru_cache
def construct_ssswages_for_county(fips):
    stat = models.SssWages.query.get_or_404(fips)
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


@jsonify_lru_cache
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


@jsonify_lru_cache
def construct_puma_for_county(fips):
    stat = models.Puma.query.get_or_404(fips)
    return {
        "pumafipsid": stat.pumafipsid,
        "fips": stat.fips,
        "pumacode": stat.pumacode,
        "areaname": stat.areaname,
        "pumaname": stat.pumaname,
        "pumapopulation": stat.pumapopulation,
        "pumaweight": stat.pumaweight
    }

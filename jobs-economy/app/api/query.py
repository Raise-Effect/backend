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

def construct_laborstats_all():
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

def construct_laborstats_for_county(fips):
    stat = models.LaborStats.query.get_or_404(fips)
        data = {
              "fips": stat.fips,
              "laborForce": stat.laborforce,
              "employed": stat.employed,
              "unemployed": stat.unemployed,
              "unemploymentRate": stat.unemploymentrate,
              "urSeasonalAdj": stat.urseasonaladj,
              "year": stat.year
        }
        return jsonify(data)

def construct_population_all():
    data = [
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
    return jsonify(data=data)

def construct_population_for_county(fips):
    stat = models.Population.query.get_or_404(fips)
    data = {
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
    return jsonify(data)

def construct_familytype_all():
    data = [
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
    return jsonify(data=data)

def construct_familytype_for_county(fips):
    stat = models.FamilyType.query.get_or_404(fips)
    data = {
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
    return jsonify(data)

def construct_wagestats_all():
    data = [
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
    return jsonify(data=data)

def construct_wagestats_for_county(fips):
    stat = models.WageStats.query.get_or_404(fips)
    data = {
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
    return jsonify(data)

def construct_calculatedstats_all():
    data = [
        {
            "fips": stat.fips,
            "percentorkids": stat.percentorkids,
            "a1allper": stat.a1allper,
            "a2allper": stat.a2allper,
            "c0allper": stat.c0allper
        }
    for stat in models.CalculatedStats.query]
    return jsonify(data=data)

def construct_calculatedstats_for_county(fips):
    stat = models.CalculatedStats.query.get_or_404(fips)
    data = {
        "fips": stat.fips,
        "percentorkids": stat.percentorkids,
        "a1allper": stat.a1allper,
        "a2allper": stat.a2allper,
        "c0allper": stat.c0allper
    }
    return jsonify(data)

def construct_sssbudget_all():
    data = [
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
    return jsonify(data=data)

def construct_sssbudget_for_county(fips):
    stat = models.SssBudget.query.get_or_404(fips)
    data = {
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
    return jsonify(data)

def construct_ssscredits_all():
    data = [
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
    return jsonify(data=data)

def construct_ssscredits_for_county(fips):
    stat = models.SssCredits.query.get_or_404(fips)
    data = {
        "ssscreditsid": stat.ssscreditsid,
        "familycode": stat.familycode,
        "oregonworkingfamilycredit": stat.oregonworkingfamilycredit,
        "earnedincometax": stat.earnedincometax,
        "childcaretax": stat.childcaretax,
        "childtax": stat.childtax,
        "fips": stat.fips,
        "year": stat.year
    }
    return jsonify(data)

def construct_ssswages_all():
    data = [
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
    return jsonify(data=data)

def construct_ssswages_for_county(fips):
    stat = models.SssWages.query.get_or_404(fips)
    data = {
        "ssswagesid": stat.ssswagesid,
        "familycode": stat.familycode,
        "hourly": stat.hourly,
        "qualifier": stat.qualifier,
        "monthly": stat.monthly,
        "annual": stat.annual,
        "fips": stat.fips,
        "year": stat.year
    }

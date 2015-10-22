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
        cache.cache_clear()


@jsonify_lru_cache()
def construct_county(fips):
    return {
        'laborStats': construct_laborstats_for_county.__wrapped__(fips),
        'populations': construct_populations_for_county.__wrapped__(fips),
        'wageStats': construct_wagestats_for_county.__wrapped__(fips),
        'calculatedStats': construct_calculatedstats_for_county.__wrapped__(fips),
        'sssBudgets': construct_sssbudgets_for_county.__wrapped__(fips),
        'sssCredits': construct_ssscredits_for_county.__wrapped__(fips),
        'sssWages': construct_ssswages_for_county.__wrapped__(fips),
        'censusHouseholds': construct_censushouseholds_for_county.__wrapped__(fips),
        'familyCodeWeights': construct_familycodeweights_for_county.__wrapped__(fips),
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
def construct_populations_all():
    return [
        {
            "fips": stat.fips,
            "population": stat.population,
            "adults": stat.adults,
            "kids": stat.kids,
            "kidsPresent": stat.kidspresentc,
            "a1c": stat.a1cc,
            "a2s2": stat.a2s2c,
            "a1c0": stat.a1c0c,
            "a1teen": stat.a1teenc,
            "kidsPresentPer": stat.kidspresentcper,
            "a1cPer": stat.a1ccper,
            "a2s2Per": stat.a2s2cper,
            "a1c0Per": stat.a1c0cper,
            "a1teenPer": stat.a1teencper,
            "minDiff": stat.mindiff,
            "mostCommonFamilyType": stat.mostcommonfamilytype,
            "year": stat.year
        } for stat in models.Population.query]


@jsonify_lru_cache()
def construct_populations_for_county(fips):
    stat = models.Population.query.filter_by(fips=fips).first_or_404()
    return {
        "fips": stat.fips,
        "population": stat.population,
        "adults": stat.adults,
        "kids": stat.kids,
        "kidsPresent": stat.kidspresentc,
        "a1c": stat.a1cc,
        "a2s2": stat.a2s2c,
        "a1c0": stat.a1c0c,
        "a1teen": stat.a1teenc,
        "kidsPresentPer": stat.kidspresentcper,
        "a1cPer": stat.a1ccper,
        "a2s2Per": stat.a2s2cper,
        "a1c0Per": stat.a1c0cper,
        "a1teenPer": stat.a1teencper,
        "minDiff": stat.mindiff,
        "mostCommonFamilyType": stat.mostcommonfamilytype,
        "year": stat.year
    }


@jsonify_lru_cache()
def construct_familytypes_all():
    return [
        {
            "familyCode": stat.familycode,
            "descriptionFc": stat.descriptionfc,
            "familyCodeRollup": stat.familycoderollup,
            "descriptionFcr": stat.descriptionfcr,
            "adults": stat.adults,
            "infants": stat.infants,
            "preschoolers": stat.preschoolers,
            "schoolAge": stat.schoolage,
            "teenagers": stat.teenagers,
            "children": stat.children
        } for stat in models.FamilyType.query]


@jsonify_lru_cache()
def construct_wagestats_all():
    return [
        {
            "fips": stat.fips,
            "householdMedianIncome": stat.householdmedianincome,
            "familyMedianIncome": stat.familymedianincome,
            "marriedMedianIncome": stat.marriedmedianincome,
            "nonFamilyMedianIncome": stat.nonfamilymedianincome,
            "lessThan10Hour": stat.lessthan10hour,
            "btwn10And15Hour": stat.btwn10and15hour,
            "totalUnder15Hour": stat.totalunder15hour,
            "percentHouseholdsBreak1": stat.percenthouseholdsbreak1,
            "percentHouseholdsBreak2": stat.percenthouseholdsbreak2,
            "percentHouseholdsBreak3": stat.percenthouseholdsbreak3,
            "percentHouseholdsBreak4": stat.percenthouseholdsbreak4,
            "percentHouseholdsBreak5": stat.percenthouseholdsbreak5,
            "percentHouseholdsBreak6": stat.percenthouseholdsbreak6,
            "percentHouseholdsBreak7": stat.percenthouseholdsbreak7,
            "percentHouseholdsBreak8": stat.percenthouseholdsbreak8,
            "percentHouseholdsBreak9": stat.percenthouseholdsbreak9,
            "percentHouseholdsBreak10": stat.percenthouseholdsbreak10,
            "year": stat.year,
        } for stat in models.WageStats.query]


@jsonify_lru_cache()
def construct_wagestats_for_county(fips, year=2013):
    stat = models.WageStats.query.filter_by(fips=fips).first_or_404()
    return {
        "fips": stat.fips,
        "householdMedianIncome": stat.householdmedianincome,
        "familyMedianIncome": stat.familymedianincome,
        "marriedMedianIncome": stat.marriedmedianincome,
        "nonFamilyMedianIncome": stat.nonfamilymedianincome,
        "lessThan10Hour": stat.lessthan10hour,
        "btwn10And15Hour": stat.btwn10and15hour,
        "totalUnder15Hour": stat.totalunder15hour,
        "percentHouseholdsBreak1": stat.percenthouseholdsbreak1,
        "percentHouseholdsBreak2": stat.percenthouseholdsbreak2,
        "percentHouseholdsBreak3": stat.percenthouseholdsbreak3,
        "percentHouseholdsBreak4": stat.percenthouseholdsbreak4,
        "percentHouseholdsBreak5": stat.percenthouseholdsbreak5,
        "percentHouseholdsBreak6": stat.percenthouseholdsbreak6,
        "percentHouseholdsBreak7": stat.percenthouseholdsbreak7,
        "percentHouseholdsBreak8": stat.percenthouseholdsbreak8,
        "percentHouseholdsBreak9": stat.percenthouseholdsbreak9,
        "percentHouseholdsBreak10": stat.percenthouseholdsbreak10,
        "year": stat.year,
    }


@jsonify_lru_cache()
def construct_calculatedstats_all():
    return [
        {
            "fips": stat.fips,
            "percentORKids": stat.percentorkids,
            "a1AllPer": stat.a1allper,
            "a2AllPer": stat.a2allper,
            "c0AllPer": stat.c0allper
        } for stat in models.CalculatedStats.query]


@jsonify_lru_cache()
def construct_calculatedstats_for_county(fips):
    stat = models.CalculatedStats.query.filter_by(fips=fips).first_or_404()
    return {
        "fips": stat.fips,
        "percentORKids": stat.percentorkids,
        "a1AllPer": stat.a1allper,
        "a2AllPer": stat.a2allper,
        "c0AllPer": stat.c0allper
    }


@jsonify_lru_cache()
def construct_sssbudgets_all():
    return [
        {
            "familyCode": stat.familycode,
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
def construct_sssbudgets_for_county(fips):
    return [
        {
            "familyCode": stat.familycode,
            "housing": stat.housing,
            "childcare": stat.childcare,
            "food": stat.food,
            "transportation": stat.transportation,
            "healthcare": stat.healthcare,
            "miscellaneous": stat.miscellaneous,
            "taxes": stat.taxes,
            "fips": stat.fips,
            "year": stat.year
        } for stat in models.SssBudget.query.filter_by(fips=fips)]


@jsonify_lru_cache()
def construct_ssscredits_all():
    return [
        {
            "familyCode": stat.familycode,
            "oregonWorkingFamilyCredit": stat.oregonworkingfamilycredit,
            "earnedIncomeTax": stat.earnedincometax,
            "childcareTax": stat.childcaretax,
            "childTax": stat.childtax,
            "fips": stat.fips,
            "year": stat.year
        } for stat in models.SssCredits.query]


@jsonify_lru_cache()
def construct_ssscredits_for_county(fips):
    return [
        {
            "familyCode": stat.familycode,
            "oregonWorkingFamilyCredit": stat.oregonworkingfamilycredit,
            "earnedIncomeTax": stat.earnedincometax,
            "childcareTax": stat.childcaretax,
            "childTax": stat.childtax,
            "fips": stat.fips,
            "year": stat.year
        } for stat in models.SssCredits.query.filter_by(fips=fips)]


@jsonify_lru_cache()
def construct_ssswages_all():
    return [
        {
            "familyCode": stat.familycode,
            "hourly": stat.hourly,
            "qualifier": stat.qualifier,
            "monthly": stat.monthly,
            "annual": stat.annual,
            "fips": stat.fips,
            "year": stat.year
        } for stat in models.SssWages.query]


@jsonify_lru_cache()
def construct_ssswages_for_county(fips):
    return [
        {
            "familyCode": stat.familycode,
            "hourly": stat.hourly,
            "qualifier": stat.qualifier,
            "monthly": stat.monthly,
            "annual": stat.annual,
            "fips": stat.fips,
            "year": stat.year
        } for stat in models.SssWages.query.filter_by(fips=fips)]


@jsonify_lru_cache()
def construct_pumas_all():
    return [
        {
            "fips": stat.fips,
            "pumaCode": stat.pumacode,
            "areaName": stat.areaname,
            "pumaName": stat.pumaname,
            "pumaPopulation": stat.pumapopulation,
            "pumaWeight": stat.pumaweight
        }
        for stat in models.Puma.query]


@jsonify_lru_cache()
def construct_pumas_for_county(fips):
    return [
        {
            "fips": stat.fips,
            "pumaCode": stat.pumacode,
            "areaName": stat.areaname,
            "pumaName": stat.pumaname,
            "pumaPopulation": stat.pumapopulation,
            "pumaWeight": stat.pumaweight
        } for stat in models.Puma.query.filter_by(fips=fips)]


@jsonify_lru_cache()
def construct_censushouseholds_all():
    return [
        {
            "fips": stat.fips,
            "totalHouseholds": stat.totalhouseholds,
            "totalMarriedFamilyHouseholds": stat.totalmarriedfamilyhouseholds,
            "totalNonFamilyHouseholds": stat.totalnonfamilyhouseholds,
            "totalUnmarriedFamilyHouseholds": stat.totalunmarriedfamilyhouseholds,
            "lowIncomeSingleParents": stat.lowincomesingleparents,
            "lowIncomeMarriedParents": stat.lowincomemarriedparents,
            "lowIncomeSingleAdults": stat.lowincomesingleadults,
            "marriedAsPercentTotal": stat.marriedaspercenttotal,
            "lowIncomeMarriedParentsAsPercentTotal": stat.lowincomemarriedparentsaspercenttotal,
            "lowIncomeMarriedParentsAsPercentMarried": stat.lowincomemarriedparentsaspercentmarried,
            "unmarriedAsPercentTotal": stat.unmarriedaspercenttotal,
            "lowIncomeSingleParentsAsPercentTotal": stat.lowincomesingleparentsaspercenttotal,
            "lowIncomeSingleParentsAsPercentUnmarried": stat.lowincomesingleparentsaspercentunmarried,
            "nonFamilyAsPercentTotal": stat.nonfamilyaspercenttotal,
            "lowIncomeSingleAdultsAsPercentTotal": stat.lowincomesingleadultsaspercenttotal,
            "lowIncomeSingleAdultsAsPercentNonFamily": stat.lowincomesingleadultsaspercentnonfamily,
        } for stat in models.CensusHousehold.query]


@jsonify_lru_cache()
def construct_censushouseholds_for_county(fips):
    stat = models.CensusHousehold.query.filter_by(fips=fips).first_or_404()
    return {
        "fips": stat.fips,
        "totalHouseholds": stat.totalhouseholds,
        "totalMarriedFamilyHouseholds": stat.totalmarriedfamilyhouseholds,
        "totalNonFamilyHouseholds": stat.totalnonfamilyhouseholds,
        "totalUnmarriedFamilyHouseholds": stat.totalunmarriedfamilyhouseholds,
        "lowIncomeSingleParents": stat.lowincomesingleparents,
        "lowIncomeMarriedParents": stat.lowincomemarriedparents,
        "lowIncomeSingleAdults": stat.lowincomesingleadults,
        "marriedAsPercentTotal": stat.marriedaspercenttotal,
        "lowIncomeMarriedParentsAsPercentTotal": stat.lowincomemarriedparentsaspercenttotal,
        "lowIncomeMarriedParentsAsPercentMarried": stat.lowincomemarriedparentsaspercentmarried,
        "unmarriedAsPercentTotal": stat.unmarriedaspercenttotal,
        "lowIncomeSingleParentsAsPercentTotal": stat.lowincomesingleparentsaspercenttotal,
        "lowIncomeSingleParentsAsPercentUnmarried": stat.lowincomesingleparentsaspercentunmarried,
        "nonFamilyAsPercentTotal": stat.nonfamilyaspercenttotal,
        "lowIncomeSingleAdultsAsPercentTotal": stat.lowincomesingleadultsaspercenttotal,
        "lowIncomeSingleAdultsAsPercentNonFamily": stat.lowincomesingleadultsaspercentnonfamily,
    }


@jsonify_lru_cache()
def construct_familycodeweights_all():
    return [
        {
            "fips": stat.fips,
            "familyCode": stat.familycode,
            "weight": stat.weight,
        }
        for stat in models.FamilyCodeWeight.query]


@jsonify_lru_cache()
def construct_familycodeweights_for_county(fips):
    return [
        {
            "fips": stat.fips,
            "familyCode": stat.familycode,
            "weight": stat.weight,
        }
        for stat in models.FamilyCodeWeight.query.filter_by(fips=fips)]

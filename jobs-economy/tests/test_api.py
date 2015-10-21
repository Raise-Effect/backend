import json
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import app
from app.api import models


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.app.test_client()
        self.db = app.db
        self.db.create_all()
        self.maxDiff = None

    def tearDown(self):
        self.db.drop_all()
        app.api.clear_caches()

    def api_get(self, path, *args, **kwargs):
        return self.app.get('/api/v1' + path, *args, **kwargs)

    def assert_json_equal(self, path, data):
        response_data = json.loads(self.api_get(path).data.decode('utf8'))
        self.assertDictEqual(response_data, data)


class PopulationTestCase(ApiTestCase):
    def test_county_list(self):
        self.db.session.add(models.County(fips=1234, county="Abc"))
        self.db.session.commit()
        self.assert_json_equal('/counties', {
            'data': [{
                'fips': 1234,
                'name': 'Abc',
            }]
        })

    def test_county_fips(self):
        self.db.session.add(models.County(fips=1234, county="Abc"))
        self.db.session.add(models.CalculatedStats(
            fips=1234,
            percentorkids=0.1,
            a1allper=0.2,
            a2allper=0.3,
            c0allper=0.4
        ))
        self.db.session.add(models.LaborStats(
            fips=1234,
            laborforce=0.1,
            employed=0.2,
            unemployed=0.3,
            unemploymentrate=0.4,
            urseasonaladj=0.5,
            year=2012
        ))
        self.db.session.add(models.Population(
            fips=1234,
            population=0.1,
            adults=0.2,
            kids=0.3,
            kidspresentc=0.4,
            a1cc=0.5,
            a2s2c=0.6,
            a1c0c=0.7,
            a1teenc=0.8,
            kidspresentcper=0.9,
            a1ccper=0.11,
            a2s2cper=0.12,
            a1c0cper=0.13,
            a1teencper=0.14,
            mindiff=0.15,
            mostcommonfamilytype='a1i0p0s0t0',
            year=2012
        ))
        self.db.session.add(models.WageStats(
            fips=1234,
            householdmedianincome=1,
            familymedianincome=2,
            marriedmedianincome=3,
            nonfamilymedianincome=4,
            lessthan10hour=0.1,
            btwn10and15hour=0.2,
            totalunder15=0.3,
            percenthouseholdsbreak1=0.4,
            percenthouseholdsbreak2=0.5,
            percenthouseholdsbreak3=0.6,
            percenthouseholdsbreak4=0.7,
            percenthouseholdsbreak5=0.8,
            percenthouseholdsbreak6=0.9,
            percenthouseholdsbreak7=0.11,
            percenthouseholdsbreak8=0.12,
            percenthouseholdsbreak9=0.13,
            percenthouseholdsbreak10=0.14,
            year=2013
        ))
        self.db.session.add(models.SssBudget(
            familycode='a1i0p0s0t0',
            housing=0.1,
            childcare=0.2,
            food=0.3,
            transportation=0.4,
            healthcare=0.5,
            miscellaneous=0.6,
            taxes=0.7,
            fips=1234,
            year=2012
        ))
        self.db.session.add(models.SssCredits(
            familycode='a1i0p0s0t0',
            oregonworkingfamilycredit=0.1,
            earnedincometax=0.2,
            childcaretax=0.3,
            childtax=0.4,
            fips=1234,
            year=2012
        ))
        self.db.session.add(models.SssWages(
            familycode='a1i0p0s0t0',
            hourly=0.1,
            qualifier="foo",
            monthly=0.2,
            annual=0.3,
            fips=1234,
            year=2012
        ))
        self.db.session.add(models.CensusHousehold(
            censushouseholdid=1,
            fips=1234,
            totalhouseholds=1,
            totalmarriedfamilyhouseholds=2,
            totalnonfamilyhouseholds=3,
            totalunmarriedfamilyhouseholds=4,
            lowincomesingleparents=5,
            lowincomemarriedparents=6,
            lowincomesingleadults=7,
            marriedaspercenttotal=0.1,
            lowincomemarriedparentsaspercenttotal=0.2,
            lowincomemarriedparentsaspercentmarried=0.3,
            unmarriedaspercenttotal=0.4,
            lowincomesingleparentsaspercenttotal=0.5,
            lowincomesingleparentsaspercentunmarried=0.6,
            nonfamilyaspercenttotal=0.7,
            lowincomesingleadultsaspercenttotal=0.8,
            lowincomesingleadultsaspercentnonfamily=0.9,
        ))
        self.db.session.add(models.FamilyCodeWeight(
            fips=1234,
            familycode='a1i0p0s0t0',
            weight=0.1,
        ))
        self.db.session.commit()
        self.assert_json_equal('/counties/1234', {
            'data': {
                'laborStats': {
                    'fips': 1234,
                    'laborForce': 0.1,
                    'employed': 0.2,
                    'unemployed': 0.3,
                    'unemploymentRate': 0.4,
                    'urSeasonalAdj': 0.5,
                    'year': 2012
                },
                'populations': {
                    'fips': 1234,
                    'population': 0.1,
                    'adults': 0.2,
                    'kids': 0.3,
                    'kidsPresent': 0.4,
                    'a1c': 0.5,
                    'a2s2': 0.6,
                    'a1c0': 0.7,
                    'a1teen': 0.8,
                    'kidsPresentPer': 0.9,
                    'a1cPer': 0.11,
                    'a2s2Per': 0.12,
                    'a1c0Per': 0.13,
                    'a1teenPer': 0.14,
                    'minDiff': 0.15,
                    'mostCommonFamilyType': 'a1i0p0s0t0',
                    'year': 2012
                },
                'wageStats': {
                    'fips': 1234,
                    'householdMedianIncome': 1,
                    'familyMedianIncome': 2,
                    'marriedMedianIncome': 3,
                    'nonFamilyMedianIncome': 4,
                    'lessThan10Hour': 0.1,
                    'btwn10And15Hour': 0.2,
                    'totalUnder15': 0.3,
                    'percentHouseholdsBreak1': 0.4,
                    'percentHouseholdsBreak2': 0.5,
                    'percentHouseholdsBreak3': 0.6,
                    'percentHouseholdsBreak4': 0.7,
                    'percentHouseholdsBreak5': 0.8,
                    'percentHouseholdsBreak6': 0.9,
                    'percentHouseholdsBreak7': 0.11,
                    'percentHouseholdsBreak8': 0.12,
                    'percentHouseholdsBreak9': 0.13,
                    'percentHouseholdsBreak10': 0.14,
                    'year': 2013
                },
                'calculatedStats': {
                    'fips': 1234,
                    'percentORKids': 0.1,
                    'a1AllPer': 0.2,
                    'a2AllPer': 0.3,
                    'c0AllPer': 0.4,
                },
                'sssBudgets': [{
                    'familyCode': 'a1i0p0s0t0',
                    'housing': 0.1,
                    'childcare': 0.2,
                    'food': 0.3,
                    'transportation': 0.4,
                    'healthcare': 0.5,
                    'miscellaneous': 0.6,
                    'taxes': 0.7,
                    'fips': 1234,
                    'year': 2012
                }],
                'sssCredits': [{
                    'familyCode': 'a1i0p0s0t0',
                    'oregonWorkingFamilyCredit': 0.1,
                    'earnedIncomeTax': 0.2,
                    'childcareTax': 0.3,
                    'childTax': 0.4,
                    'fips': 1234,
                    'year': 2012
                }],
                'sssWages': [{
                    'familyCode': 'a1i0p0s0t0',
                    'hourly': 0.1,
                    'qualifier': "foo",
                    'monthly': 0.2,
                    'annual': 0.3,
                    'fips': 1234,
                    'year': 2012
                }],
                'censusHouseholds': {
                    "fips": 1234,
                    "totalHouseholds": 1,
                    "totalMarriedFamilyHouseholds": 2,
                    "totalNonFamilyHouseholds": 3,
                    "totalUnmarriedFamilyHouseholds": 4,
                    "lowIncomeSingleParents": 5,
                    "lowIncomeMarriedParents": 6,
                    "lowIncomeSingleAdults": 7,
                    "marriedAsPercentTotal": 0.1,
                    "lowIncomeMarriedParentsAsPercentTotal": 0.2,
                    "lowIncomeMarriedParentsAsPercentMarried": 0.3,
                    "unmarriedAsPercentTotal": 0.4,
                    "lowIncomeSingleParentsAsPercentTotal": 0.5,
                    "lowIncomeSingleParentsAsPercentUnmarried": 0.6,
                    "nonFamilyAsPercentTotal": 0.7,
                    "lowIncomeSingleAdultsAsPercentTotal": 0.8,
                    "lowIncomeSingleAdultsAsPercentNonFamily": 0.9,
                },
                'familyCodeWeights': [{
                    "fips": 1234,
                    "familyCode": "a1i0p0s0t0",
                    "weight": 0.1,
                }]
            }
        })

    def test_calculatedstats_all_counties(self):
        self.db.session.add(models.CalculatedStats(
            fips=1234,
            percentorkids=0.1,
            a1allper=0.2,
            a2allper=0.3,
            c0allper=0.4
        ))
        self.assert_json_equal('/counties/calculatedstats', {
            'data': [{
                'fips': 1234,
                'percentORKids': 0.1,
                'a1AllPer': 0.2,
                'a2AllPer': 0.3,
                'c0AllPer': 0.4,
            }]
        })

    def test_populations_all_counties(self):
        self.db.session.add(models.Population(
            fips=1234,
            population=0.1,
            adults=0.2,
            kids=0.3,
            kidspresentc=0.4,
            a1cc=0.5,
            a2s2c=0.6,
            a1c0c=0.7,
            a1teenc=0.8,
            kidspresentcper=0.9,
            a1ccper=0.11,
            a2s2cper=0.12,
            a1c0cper=0.13,
            a1teencper=0.14,
            mindiff=0.15,
            mostcommonfamilytype='a1i0p0s0t0',
            year=2012
        ))
        self.assert_json_equal('/counties/populations', {
            'data': [{
                'fips': 1234,
                'population': 0.1,
                'adults': 0.2,
                'kids': 0.3,
                'kidsPresent': 0.4,
                'a1c': 0.5,
                'a2s2': 0.6,
                'a1c0': 0.7,
                'a1teen': 0.8,
                'kidsPresentPer': 0.9,
                'a1cPer': 0.11,
                'a2s2Per': 0.12,
                'a1c0Per': 0.13,
                'a1teenPer': 0.14,
                'minDiff': 0.15,
                'mostCommonFamilyType': 'a1i0p0s0t0',
                'year': 2012
            }]
        })

    def test_laborstats_all_counties(self):
        self.db.session.add(models.LaborStats(
            fips=1234,
            laborforce=0.1,
            employed=0.2,
            unemployed=0.3,
            unemploymentrate=0.4,
            urseasonaladj=0.5,
            year=2012
        ))
        self.assert_json_equal('/counties/laborstats', {
            'data': [{
                'fips': 1234,
                'laborForce': 0.1,
                'employed': 0.2,
                'unemployed': 0.3,
                'unemploymentRate': 0.4,
                'urSeasonalAdj': 0.5,
                'year': 2012
            }]
        })

    def test_wagestats_all_counties(self):
        self.db.session.add(models.WageStats(
            fips=1234,
            householdmedianincome=1,
            familymedianincome=2,
            marriedmedianincome=3,
            nonfamilymedianincome=4,
            lessthan10hour=0.1,
            btwn10and15hour=0.2,
            totalunder15=0.3,
            percenthouseholdsbreak1=0.4,
            percenthouseholdsbreak2=0.5,
            percenthouseholdsbreak3=0.6,
            percenthouseholdsbreak4=0.7,
            percenthouseholdsbreak5=0.8,
            percenthouseholdsbreak6=0.9,
            percenthouseholdsbreak7=0.11,
            percenthouseholdsbreak8=0.12,
            percenthouseholdsbreak9=0.13,
            percenthouseholdsbreak10=0.14,
            year=2013
        ))
        self.assert_json_equal('/counties/wagestats',
        {
            'data': [{
                'fips': 1234,
                'householdMedianIncome': 1,
                'familyMedianIncome': 2,
                'marriedMedianIncome': 3,
                'nonFamilyMedianIncome': 4,
                'lessThan10Hour': 0.1,
                'btwn10And15Hour': 0.2,
                'totalUnder15': 0.3,
                'percentHouseholdsBreak1': 0.4,
                'percentHouseholdsBreak2': 0.5,
                'percentHouseholdsBreak3': 0.6,
                'percentHouseholdsBreak4': 0.7,
                'percentHouseholdsBreak5': 0.8,
                'percentHouseholdsBreak6': 0.9,
                'percentHouseholdsBreak7': 0.11,
                'percentHouseholdsBreak8': 0.12,
                'percentHouseholdsBreak9': 0.13,
                'percentHouseholdsBreak10': 0.14,
                'year': 2013
            }]
        })

    def test_sssbudgets_all_counties(self):
        self.db.session.add(models.SssBudget(
            familycode='a1i0p0s0t0',
            housing=0.1,
            childcare=0.2,
            food=0.3,
            transportation=0.4,
            healthcare=0.5,
            miscellaneous=0.6,
            taxes=0.7,
            fips=1234,
            year=2012
        ))
        self.assert_json_equal('/counties/sssbudgets', {
            'data': [
                {
                    'familyCode': 'a1i0p0s0t0',
                    'housing': 0.1,
                    'childcare': 0.2,
                    'food': 0.3,
                    'transportation': 0.4,
                    'healthcare': 0.5,
                    'miscellaneous': 0.6,
                    'taxes': 0.7,
                    'fips': 1234,
                    'year': 2012
                }
            ]
        })

    def test_ssscredits_all_counties(self):
        self.db.session.add(models.SssCredits(
            familycode='a1i0p0s0t0',
            oregonworkingfamilycredit=0.1,
            earnedincometax=0.2,
            childcaretax=0.3,
            childtax=0.4,
            fips=1234,
            year=2012
        ))
        self.assert_json_equal('/counties/ssscredits', {
            'data': [
                {
                    'familyCode': 'a1i0p0s0t0',
                    'oregonWorkingFamilyCredit': 0.1,
                    'earnedIncomeTax': 0.2,
                    'childcareTax': 0.3,
                    'childTax': 0.4,
                    'fips': 1234,
                    'year': 2012
                }
            ]
        })

    def test_ssswages_all_counties(self):
        self.db.session.add(models.SssWages(
            familycode='a1i0p0s0t0',
            hourly=0.1,
            qualifier="foo",
            monthly=0.2,
            annual=0.3,
            fips=1234,
            year=2012
        ))
        self.assert_json_equal('/counties/ssswages', {
            'data': [
                {
                    'familyCode': 'a1i0p0s0t0',
                    'hourly': 0.1,
                    'qualifier': "foo",
                    'monthly': 0.2,
                    'annual': 0.3,
                    'fips': 1234,
                    'year': 2012
                }
            ]
        })

    def test_pumas_all_counties(self):
        self.db.session.add(models.Puma(
            fips=1234,
            pumacode=5678,
            areaname="area-name",
            pumaname="puma-name",
            pumapopulation=0.1,
            pumaweight=0.2
        ))
        self.assert_json_equal('/counties/pumas', {
            "data": [
                {
                    "fips": 1234,
                    "pumaCode": 5678,
                    "areaName": "area-name",
                    "pumaName": "puma-name",
                    "pumaPopulation": 0.1,
                    "pumaWeight": 0.2,
                }
            ]
        })


    def test_censushouseholds_all_counties(self):
        self.db.session.add(models.CensusHousehold(
            fips=1234,
            lowincomesingleadults=1,
            totalsingleadults=2,
            lowincomesingleparents=3,
            totalsingleparents=4,
            lowincomemarriedparents=5,
            totalmarriedparents=6,
            totalhouseholds=7
        ))
        self.db.session.commit()
        self.assert_json_equal('/counties/censushouseholds', {
            "data": [{
                "fips": 1234,
                "totalHouseholds": 1,
                "totalMarriedFamilyHouseholds": 2,
                "totalNonFamilyHouseholds": 3,
                "totalUnmarriedFamilyHouseholds": 4,
                "lowIncomeSingleParents": 5,
                "lowIncomeMarriedParents": 6,
                "lowIncomeSingleAdults": 7,
                "marriedAsPercentTotal": 0.1,
                "lowIncomeMarriedParentsAsPercentTotal": 0.2,
                "lowIncomeMarriedParentsAsPercentMarried": 0.3,
                "unmarriedAsPercentTotal": 0.4,
                "lowIncomeSingleParentsAsPercentTotal": 0.5,
                "lowIncomeSingleParentsAsPercentUnmarried": 0.6,
                "nonFamilyAsPercentTotal": 0.7,
                "lowIncomeSingleAdultsAsPercentTotal": 0.8,
                "lowIncomeSingleAdultsAsPercentNonFamily": 0.9,
            }]
        })

    def test_censushouseholds_for_county(self):
        self.db.session.add(models.CensusHousehold(
            fips=1234,
            lowincomesingleadults=1,
            totalsingleadults=2,
            lowincomesingleparents=3,
            totalsingleparents=4,
            lowincomemarriedparents=5,
            totalmarriedparents=6,
            totalhouseholds=7
        ))
        self.db.session.commit()
        self.assert_json_equal('/counties/1234/censushouseholds', {
            "data": {
                "fips": 1234,
                "totalHouseholds": 1,
                "totalMarriedFamilyHouseholds": 2,
                "totalNonFamilyHouseholds": 3,
                "totalUnmarriedFamilyHouseholds": 4,
                "lowIncomeSingleParents": 5,
                "lowIncomeMarriedParents": 6,
                "lowIncomeSingleAdults": 7,
                "marriedAsPercentTotal": 0.1,
                "lowIncomeMarriedParentsAsPercentTotal": 0.2,
                "lowIncomeMarriedParentsAsPercentMarried": 0.3,
                "unmarriedAsPercentTotal": 0.4,
                "lowIncomeSingleParentsAsPercentTotal": 0.5,
                "lowIncomeSingleParentsAsPercentUnmarried": 0.6,
                "nonFamilyAsPercentTotal": 0.7,
                "lowIncomeSingleAdultsAsPercentTotal": 0.8,
                "lowIncomeSingleAdultsAsPercentNonFamily": 0.9,
            }
        })

    def test_county_404(self):
        self.assert_json_equal('/counties/1/', {
            'errorMessage': 'Not found: http://localhost/api/v1/counties/1/',
            'status': 404,
        })
        self.assertEqual(self.api_get('/counties/1/').status, "404 NOT FOUND")

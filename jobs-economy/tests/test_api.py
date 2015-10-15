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
        self.assert_json_equal('/counties/', {
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
            medianwage=0.1,
            medianhourly=0.2,
            lessthan10hour=0.3,
            btwn10and15hour=0.4,
            totalunder15=0.5,
            totalpercentorjobs=0.6,
            countysalary=0.7,
            countywage=0.8,
            countywageh2=0.9,
            countywagerank=0.11,
            countywageh2rank=0.12,
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
                'population': {
                    'fips': 1234,
                    'population': 0.1,
                    'adults': 0.2,
                    'kids': 0.3,
                    'kidspresentc': 0.4,
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
                    'medianWage': 0.1,
                    'medianHourly': 0.2,
                    'lessThan10Hour': 0.3,
                    'btwn10And15Hour': 0.4,
                    'totalUnder15': 0.5,
                    'totalPercentORJobs': 0.6,
                    'countySalary': 0.7,
                    'countyWage': 0.8,
                    'countyWageH2': 0.9,
                    'countyWageRank': 0.11,
                    'countyWageH2Rank': 0.12,
                    'year': 2013
                },
                'calculatedStats': {
                    'fips': 1234,
                    'percentORKids': 0.1,
                    'a1AllPer': 0.2,
                    'a2AllPer': 0.3,
                    'c0AllPer': 0.4,
                },
                'sssBudget': {
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
                },
                'sssCredits': {
                    'familyCode': 'a1i0p0s0t0',
                    'oregonWorkingFamilyCredit': 0.1,
                    'earnedIncomeTax': 0.2,
                    'childcareTax': 0.3,
                    'childTax': 0.4,
                    'fips': 1234,
                    'year': 2012
                },
                'sssWages': {
                    'familyCode': 'a1i0p0s0t0',
                    'hourly': 0.1,
                    'qualifier': "foo",
                    'monthly': 0.2,
                    'annual': 0.3,
                    'fips': 1234,
                    'year': 2012
                }
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

    def test_population_all_counties(self):
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
        self.assert_json_equal('/counties/population', {
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
            medianwage=0.1,
            medianhourly=0.2,
            lessthan10hour=0.3,
            btwn10and15hour=0.4,
            totalunder15=0.5,
            totalpercentorjobs=0.6,
            countysalary=0.7,
            countywage=0.8,
            countywageh2=0.9,
            countywagerank=0.11,
            countywageh2rank=0.12,
            year=2013
        ))
        self.assert_json_equal('/counties/wagestats', {
            'data': [{
                'fips': 1234,
                'medianWage': 0.1,
                'medianHourly': 0.2,
                'lessThan10Hour': 0.3,
                'btwn10And15Hour': 0.4,
                'totalUnder15': 0.5,
                'totalPercentORJobs': 0.6,
                'countySalary': 0.7,
                'countyWage': 0.8,
                'countyWageH2': 0.9,
                'countyWageRank': 0.11,
                'countyWageH2Rank': 0.12,
                'year': 2013
            }]
        })

    def test_sssbudget_all_counties(self):
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
        self.assert_json_equal('/counties/sssbudget', {
            'data': [{
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
            }]
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
            'data': [{
                'familyCode': 'a1i0p0s0t0',
                'oregonWorkingFamilyCredit': 0.1,
                'earnedIncomeTax': 0.2,
                'childcareTax': 0.3,
                'childTax': 0.4,
                'fips': 1234,
                'year': 2012
            }]
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
            'data': [{
                'familyCode': 'a1i0p0s0t0',
                'hourly': 0.1,
                'qualifier': "foo",
                'monthly': 0.2,
                'annual': 0.3,
                'fips': 1234,
                'year': 2012
            }]
        })

    def test_puma_all_counties(self):
        pass

    def test_county_404(self):
        self.assert_json_equal('/counties/1', {
            'errorMessage': 'Not found: http://localhost/api/v1/counties/1',
            'status': 404,
        })
        self.assertEqual(self.api_get('/counties/1').status, "404 NOT FOUND")

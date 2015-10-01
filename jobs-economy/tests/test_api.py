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
        self.db.session.add(models.CalculatedStats(fips=1234,
            percentorkids=0.1,
            a1allper=0.2,
            a2allper=0.3,
            c0allper=0.4))

        self.db.session.commit()
        self.assert_json_equal('/counties/1234', {
            'data': {
                'fips': 1234,
                'name': 'Abc',
            }
        })

    def test_county_404(self):
        self.assert_json_equal('/counties/1', {
            'errorMessage': 'Not found: http://localhost/api/v1/counties/1',
            'status': 404,
        })
        self.assertEqual(self.api_get('/counties/1').status, "404 NOT FOUND")

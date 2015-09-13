import app
import json
import unittest


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def api_get(self, path, *args, **kwargs):
        return self.app.get('/api/v1' + path, *args, **kwargs)

    def assert_json_equal(self, path, data):
        self.assertDictEqual(json.loads(self.api_get(path).data), data)


class PopulationTestCase(ApiTestCase):
    def test_county_list(self):
        self.assert_json_equal('/counties', {
            'data': []
        })

    def test_county_fips(self):
        self.assert_json_equal('/counties/#####', {
            'data': []
        })

    def test_county_404(self):
        self.assert_json_equal('/counties/1', {
            'error': 'Not found'
        })
        self.assertEqual(self.api_get('/counties/1').status, 404)

import unittest
from common import API_KEY
from api import FinnhubAPI

class FinnhubAPITestCase(unittest.TestCase):

    def setUp(self):
        self.finnhub_api = FinnhubAPI(API_KEY)

    def test_quote_valid_symbol(self):
        response = self.finnhub_api.get_quote('amd')
        self.assertTrue(response['c'] > 0.00)

    def test_quote_invalid_symbol(self):
        response = self.finnhub_api.get_quote('xxx')
        self.assertEqual(response['d'], None)
        self.assertEqual(response['c'], 0)

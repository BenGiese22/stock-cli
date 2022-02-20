import unittest
from common import API_KEY
from stock_api import StockAPI

class TestStockAPICase(unittest.TestCase):

    def setUp(self):
        self.stock_api = StockAPI(API_KEY)

    def test_validate_valid_symbol(self):
        is_valid = self.stock_api.validate_symbol('amd')
        self.assertTrue(is_valid)

    def test_validate_invalid_symbol(self):
        is_valid = self.stock_api.validate_symbol('xxx')
        self.assertFalse(is_valid)

    def test_quote_valid_symbol(self):
        response = self.stock_api.get_quote('amd')
        self.assertTrue(response['c'] > 0.00)

    def test_quote_invalid_symbol(self):
        response = self.stock_api.get_quote('xxx')
        self.assertEqual(response['d'], None)
        self.assertEqual(response['c'], 0)

    def test_intraday(self):
        response = self.stock_api.get_intraday('amd')
        self.assertEqual(type(response), list)

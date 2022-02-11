import unittest
import json
import util

# TEST_RESPONSE = {
#     'Meta Data': {
#         '1. Information': 'Intraday (5min) open, high, low, close prices and volume',
#         '2. Symbol': 'AMD',
#         '3. Last Refreshed': '2022-02-10 20:00:00',
#         '4. Interval': '5min',
#         '5. Output Size': 'Compact',
#         '6. Time Zone': 'US/Eastern'
#     },
#     'Time Series (5min)': {
        
#         '2022-02-10 20:00:00': {'1. open': '124.8300', '2. high': '124.8800', '3. low': '124.7500', '4. close': '124.7500', '5. volume': '12625'},
#         '2022-02-10 19:55:00': {'1. open': '124.8000', '2. high': '124.8700', '3. low': '124.7800', '4. close': '124.7900', '5. volume': '7829'},
#         '2022-02-10 19:50:00': {'1. open': '124.8000', '2. high': '124.8100', '3. low': '124.7500', '4. close': '124.7600', '5. volume': '11513'}
#     }
# }
TEST_QUOTE = {'c': 121.8999, 'd': -3.8701, 'dp': -3.0771, 'h': 127.1699, 'l': 121.43, 'o': 126.14, 'pc': 125.77, 't': 1644592897}

class UtilTestCase(unittest.TestCase):

    def test_get_data(self):


if __name__ == '__main__':
    unittest.main()

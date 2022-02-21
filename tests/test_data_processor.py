import unittest
from data_processor import DataProcessor

INTRADAY_DATA = {
    'Time Series (5min)': {
       
    },  
}

MONTHLY_DATA = {
    'Monthly Time Series': {
        '2022-02-18': {'1. open': '116.7500', '2. high': '132.9600', '3. low': '109.8900', '4. close': '113.8300', '5. volume': '1636428145'},
        '2022-01-31': {'1. open': '145.1350', '2. high': '152.4200', '3. low': '99.3500', '4. close': '114.2500', '5. volume': '1637852102'},
        '2021-12-31': {'1. open': '160.3700', '2. high': '160.8800', '3. low': '130.6000', '4. close': '143.9000', '5. volume': '1175268948'}
    },  
}

class DataProcessorTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.data_processor = DataProcessor()

    def test_intraday_data(self) -> None:
        pass

    def test_monthly_data(self) -> None:
        data, dts = self.data_processor.process_data(MONTHLY_DATA)
        self.assertEqual(dts[0], '31/12/2021 00:00:00da')
        self.assertEqual(data[0], 143.90)


import finnhub
import requests
from data_processor import DataProcessor
from typing import Tuple
from common import FINNHUB_API_KEY, ALPHA_VANTAGE_API_KEY, TimeSeries

class StockAPI:

    def __init__(self) -> None:
        self.finnhub_client = finnhub.Client(api_key=FINNHUB_API_KEY)
        self.data_processor = DataProcessor()

    def validate_symbol(self, symbol: str) -> bool:
        response = self.finnhub_client.symbol_lookup(symbol)
        results = response['result']
        for result in results:
            result_symbol = result['symbol']
            if result_symbol.lower() == symbol:
                return True
        return False

    def get_quote(self, symbol: str) -> dict:
        return self.finnhub_client.quote(symbol.upper())

    def get_intraday(self, symbol: str) -> Tuple[list, list]:
        r = requests.get(self._get_time_series_url(TimeSeries.INTRADAY, symbol))
        data = r.json()
        processed_data, dts = self.data_processor.process_data(data)
        return processed_data, dts

    def get_monthly(self, symbol: str) -> Tuple[list, list]:
        r = requests.get(self._get_time_series_url(TimeSeries.MONTHLY, symbol))
        data = r.json()
        processed_data, dts = self.data_processor.process_data(data)
        return processed_data, dts

    def _get_time_series_url(self, time_series: TimeSeries, symbol: str) -> str:
        interval = ""
        if time_series is TimeSeries.INTRADAY:
            interval = "&interval=5min"
        return f"https://www.alphavantage.co/query?function={time_series.value}&symbol={symbol}{interval}&apikey={ALPHA_VANTAGE_API_KEY}"

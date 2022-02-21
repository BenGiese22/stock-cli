import finnhub
import requests
from data_processor import DataProcessor
from typing import Tuple
from common import FINNHUB_API_KEY, ALPHA_VANTAGE_API_KEY

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
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={ALPHA_VANTAGE_API_KEY}"
        r = requests.get(url)
        data = r.json()
        processed_data, dts = self.data_processor.process_intraday_data(data)
        return processed_data, dts

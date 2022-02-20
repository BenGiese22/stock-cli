import finnhub
import requests
from data_processor import DataProcessor

class StockAPI:

    def __init__(self, api_key: str) -> None:
        self.client = finnhub.Client(api_key=api_key)
        self.data_processor = DataProcessor()

    def validate_symbol(self, symbol: str) -> bool:
        response = self.client.symbol_lookup(symbol)
        results = response['result']
        for result in results:
            result_symbol = result['symbol']
            if result_symbol.lower() == symbol:
                return True
        return False

    def get_quote(self, symbol: str) -> dict:
        return self.client.quote(symbol.upper())

    def get_intraday(self, symbol: str) -> dict:
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AMD&interval=5min&apikey=T9N0WM17ULYZHHPM'
        r = requests.get(url)
        data = r.json()
        processed_data = self.data_processor.process_intraday_data(data)
        return processed_data

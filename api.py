import requests

from enums.interval import Interval


class StockAPI:

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def intraday(self, symbol: str, interval: Interval) -> dict:
        # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol.upper()}&interval={interval.value}&apikey={self.api_key}"
        
        r = requests.get(url)
        data = r.json()

        # TODO error handling. 

        print(data)

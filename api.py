import finnhub

class FinnhubAPI:

    def __init__(self, api_key: str) -> None:
        self.client = finnhub.Client(api_key=api_key)

    def get_quote(self, symbol: str) -> dict:
        return self.client.quote(symbol.upper())

import finnhub

class StockAPI:

    def __init__(self, api_key: str) -> None:
        self.client = finnhub.Client(api_key=api_key)

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

import click
from api import StockAPI
from enums.interval import Interval

API_KEY = 'T9N0WM17ULYZHHPM'

@click.command()
def stock_cli() -> None:
    stock_api = StockAPI(API_KEY)
    stock_api.intraday('amd', Interval.ONE_MIN)

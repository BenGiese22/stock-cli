import globals
from events.event import Event
from stock_api import StockAPI
from common import API_KEY

class AddToWatchlistEvent(Event):

    def __init__(self):
        super().__init__()
        self.stock_api = StockAPI(API_KEY)

    def start_event(self) -> None:
        valid_symbol = False
        while not valid_symbol:   
            self.window.erase()
            self.window.refresh()
            self.window.addstr(0,0, "Enter Stock Symbol\n--> ")
            self.curses_config.echo()
            self.curses_config.set_cursor(1)
            _input = self.window.getstr().decode('utf-8-sig')
            self.curses_config.set_cursor(0)
            self.curses_config.noecho()
            valid_symbol = self.stock_api.validate_symbol(_input)
        globals.WATCHLIST.append(_input)


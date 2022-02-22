import time
import globals
from threading import Thread
from typing import Callable
from events.base_event import BaseEvent
from stock_api import StockAPI
from common import TimeSeries
import plotext as plt

class GraphEvent(BaseEvent):

    def __init__(self):
        super().__init__()
        self.stock_api = StockAPI()
        self.commands = [
            {
                'command_name': 'View Intraday Graph',
                'command_func': self.view_intraday_graph_command
            },
            {
                'command_name': 'View Monthly Graph',
                'command_func': self.view_monthly_graph_command
            }
        ]

    def view_intraday_graph_command(self) -> None:
        self.start_event(TimeSeries.INTRADAY)

    def view_monthly_graph_command(self) -> None:
        self.start_event(TimeSeries.MONTHLY)

    def start_event(self, time_series: TimeSeries):
        self._specify_symbol()
        self.curses_config.disable()
        event_func = self._get_event_func(time_series)
        self.thread = Thread(target=event_func, name='graph_thread', args=(lambda: globals.KEY_LISTENER_HIT, ))
        self.thread.start()
        self.keyboard_controller.start_listener(self.quit_event)

    def _get_event_func(self, time_series: TimeSeries) -> Callable:
        if time_series is TimeSeries.INTRADAY:
            return self.run_intraday_event
        return self.run_monthly_event

    def quit_event(self, key):
        try:
            if key.char == 'q':
                plt.clear_plot()
                plt.clear_terminal()
                self.keyboard_controller.stop_listener('backspace')
                self.thread.join()
                self.curses_config.init_window()
        except AttributeError as ae:
            pass

    def _specify_symbol(self) -> None:
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
        globals.GRAPH_SYMBOL = _input.lower()

    def run_intraday_event(self, key_listen):
        self.init_intraday_plot()
        while True:
            time.sleep(1.00 - ((time.time() - self.starttime) % 1.00))
            if key_listen():
                break

    def run_monthly_event(self, key_listen):
        self.init_monthly_plot()
        while True:
            time.sleep(1.00 - ((time.time() - self.starttime) % 1.00))
            if key_listen():
                break

    def init_intraday_plot(self) -> None:
        stock_data, datetimes = self.stock_api.get_intraday(globals.GRAPH_SYMBOL.lower())
        plt.plot_date(datetimes, stock_data)
        plt.title(globals.GRAPH_SYMBOL.upper())
        plt.xlabel("Intraday")
        plt.ylabel("Stock Price $")
        plt.clear_terminal()
        plt.show()

    def init_monthly_plot(self) -> None:
        stock_data, datetimes = self.stock_api.get_monthly(globals.GRAPH_SYMBOL.lower())
        plt.plot_date(datetimes, stock_data)
        plt.title(globals.GRAPH_SYMBOL.upper())
        plt.xlabel("Monthly")
        plt.ylabel("Stock Price $")
        plt.clear_terminal()
        plt.show()

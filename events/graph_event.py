import time
import os
import globals
from threading import Thread
from events.event import Event
from stock_api import StockAPI
from common import API_KEY
import plotext as plt

class GraphEvent(Event):

    def __init__(self):
        super().__init__()
        self.stock_api = StockAPI(API_KEY)


    def specify_symbol(self) -> None:
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

    def start_event(self):
        self.specify_symbol()
        self.curses_config.disable()
        self.thread = Thread(target=self.run_event, name='graph_thread', args=(lambda: globals.KEY_LISTENER_HIT, ))
        self.thread.start()
        self.keyboard_controller.start_listener(self.quit_event)

    def quit_event(self, key):
        try:
            if key.char == 'q':
                self.keyboard_controller.stop_listener('backspace')
                self.thread.join()
                self.curses_config.init_window()
        except AttributeError as ae:
            pass

    def run_event(self, key_listen):
        size = os.get_terminal_size()
        y = plt.sin() # sinusoidal signal 
        # plt.limit_size(size.columns-10, size.lines-10)
        plt.scatter(y)
        plt.title(globals.GRAPH_SYMBOL.upper())
        plt.clear_terminal()
        plt.show()
        while True:
            time.sleep(1.00 - ((time.time() - self.starttime) % 1.00))
            if key_listen():
                break

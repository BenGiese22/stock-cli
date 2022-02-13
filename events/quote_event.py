import time
import globals
from threading import Thread
from typing import Callable
from event import Event

class QuoteEvent(Event):

    def __init__(self):
        super().__init__()

    def start_event(self):
        self.window.addstr(0,0, f"Enter stock symbol.\n--> ")
        self.curses_config.echo()
        _input = self.window.getstr().decode('utf-8-sig')
        self.curses_config.noecho()
        self.window.erase()
        self.window.refresh()

        # TODO check if valid symbol
        # self.thread_manager.add_thread(self.run_event, 'quote_thread', _input)
        self.thread = Thread(target=self.run_event, name='quote_thread', args=(lambda: globals.KEY_LISTENER_HIT, _input))
        self.keyboard_controller.start_listener(self.quit_event)
        self.thread.start()

    def quit_event(self, key):
        if key.char == 'q':
            self.keyboard_controller.stop_listener('backspace')
            # self.thread_manager.join_thread('quote_thread')
            self.thread.join()

    def run_event(self, key_listen, stock_symbol):
        self.curses_config.set_cursor(0)
        x = 0
        while True:
            self.window.addstr(0, 0, f"hit - {x} - {stock_symbol}", self.curses_config.get_green_color_pair())
            time.sleep(1.00 - ((time.time() - self.starttime) % 1.00))
            self.window.refresh()
            x += 1
            if key_listen():
                self.curses_config.set_cursor(1)
                break

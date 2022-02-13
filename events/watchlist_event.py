import time
import globals
from threading import Thread
from events.event import Event
from stock_api import StockAPI
from common import API_KEY

class WatchlistEvent(Event):

    def __init__(self):
        super().__init__()
        self.stock_api = StockAPI(API_KEY)


    def start_event(self):
        self.thread = Thread(target=self.run_event, name='watchlist_thread', args=(lambda: globals.KEY_LISTENER_HIT, ))
        self.thread.start()
        self.keyboard_controller.start_listener(self.quit_event)

    def quit_event(self, key):
        try:
            if key.char == 'q':
                self.keyboard_controller.stop_listener('backspace')
                self.thread.join()
        except AttributeError as ae:
            pass

    def run_event(self, key_listen):
        self.window.erase()
        self.window.refresh()
        x = 0
        while True:
            self.window.addstr(0, 0, f"hit - {x} - {'amd'}", self.curses_config.get_green_color_pair())
            time.sleep(1.00 - ((time.time() - self.starttime) % 1.00))
            self.window.refresh()
            x += 1
            if key_listen():
                break

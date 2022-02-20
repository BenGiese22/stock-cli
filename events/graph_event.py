import time
import os
import globals
from threading import Thread
from events.event import Event
from stock_api import StockAPI
from common import API_KEY
import plotext as plt
# from curses_config import CursesConfig
# import termplotlib as tpl
# import numpy as np

class GraphEvent(Event):

    def __init__(self):
        super().__init__()
        self.stock_api = StockAPI(API_KEY)


    def start_event(self):
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
        # CursesConfig.pause_curses()
        # self.window.erase()
        # self.window.refresh()
        y = plt.sin() # sinusoidal signal 
        # plt.limit_size(size.columns-10, size.lines-10)
        plt.scatter(y)
        plt.title("Scatter Plot")
        plt.clear_terminal()
        plt.show()
        # x = np.linspace(0, 2*np.pi, 100)
        # y = np.sin(x) + x
        # fig = tpl.figure()
        # fig.plot(x,y, width=size.columns, height=size.lines)
        # fig.show()
        while True:
            time.sleep(1.00 - ((time.time() - self.starttime) % 1.00))
            if key_listen():
                break

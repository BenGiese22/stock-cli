import time
from keyboard_controller import KeyboardController
from curses_config import CursesConfig
import threading

EVENT_NAMES = ['watchlist_thread']

class Event:

    def __init__(self):
        self.keyboard_controller = KeyboardController()
        self.curses_config = CursesConfig()
        self.window = self.curses_config.init_window()
        self.starttime = time.time()   

    def start_event(self):
        pass

    def stop_event(self):
        pass

    def run_event(self):
        pass

    def is_master_thread(self) -> bool:
        for thread in threading.enumerate():
            thread_name = thread.name
            if thread_name in EVENT_NAMES:
                return True
        return False
                

    def get_master_input(self) -> str:
        self.window.erase()
        self.window.refresh()
        self.window.addstr(0,0, "Commands:")
        self.window.addstr(1,0, "- 'x' to exit.")
        self.window.addstr(2,0, "- 'w' to view watchlist.")
        self.window.addstr(3,0, "- 'a' to add symbol to watchlist.")
        self.curses_config.noecho()
        _input = self.window.getkey()
        self.curses_config.echo()
        return _input

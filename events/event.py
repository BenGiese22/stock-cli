import time
from thread_manager import ThreadManager
from keyboard_controller import KeyboardController
from curses_config import CursesConfig


class Event:

    def __init__(self):
        self.thread_manager = ThreadManager()
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

    @staticmethod
    def get_master_input(self) -> str:
        self.window.addstr(0,0, "Press 'n' to view a stock's price or 'exit' to exit program.")
        self.window.addstr(1,0, "--> ")
        self.curses_config.echo()
        _input = self.window.getstr().decode('utf-8-sig')
        self.curses_config.noecho()
        self.window.erase()
        self.window.refresh()
        return _input

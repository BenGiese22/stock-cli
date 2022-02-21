import time
from keyboard_controller import KeyboardController
from curses_config import CursesConfig
import threading

EVENT_NAMES = ['watchlist_thread', 'graph_thread']

COMMANDS = {
    'basic': {
        'commands': [
            "Basic Commands:",
            "- 'x' to exit."
        ]
    },
    'watchlist': {
        'commands': [
            "Watchlist Commands:",
            "- 'w' to view watchlist.",
            "  - press 'q' while in watchlist view to exit.",
            "- 'n' to add symbol to watchlist.",
            "- 'd' to remove symbol from watchlist."
        ]
    },
    'graph': {
        'commands': [
            "Graph Commands:",
            "- 'g' to view intraday graph of symbol.",
            "- 'm' to view monthly graph of symbol.",
            "  - press 'q' while in graph view to exit."
        ]
    }
}

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
                

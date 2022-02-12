from curses_config import CursesConfig
from thread_manager import ThreadManager
from keyboard import Keyboard


def init() -> None:
    global curses_config
    global thread_manager
    global STDSCR
    global KEY_LISTEN
    global keyboard
    curses_config = CursesConfig()
    thread_manager = ThreadManager()
    STDSCR = curses_config.init_curses()
    KEY_LISTEN = False
    keyboard = Keyboard()


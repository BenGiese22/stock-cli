import time
import sys
import atexit
import curses
import globals
from traceback import print_exc
from api import FinnhubAPI
from common import API_KEY
from curses_config import CursesConfig

curses_config = CursesConfig()
STDSCR = curses_config.init_curses()
starttime = time.time()

# TODO write low opacity press q to exit?
def run(key_listen):
    curses.curs_set(0)
    try:
        x = 0
        while True:
            STDSCR.addstr(0, 0, f"hit - {x}", curses_config.get_green_color_pair())
            time.sleep(1.00 - ((time.time() - starttime) % 1.00))
            STDSCR.refresh()
            x += 1
            if key_listen():
                curses.curs_set(1)
                break
    except BaseException as ex:
        print_exc()

    
def on_press(key):
    try:
        if key.char == 'q':
            globals.keyboard.stop_listener('backspace')
            globals.KEY_LISTENER_HIT = True
            globals.thread_manager.join_thread('quote_thread')
            globals.KEY_LISTENER_HIT = False
    except AttributeError:
        print_exc()
    except BaseException:
        print_exc()

def start_quote_thread() -> None:
    STDSCR.addstr(0,0, f"Enter stock symbol.\n--> ")
    curses.echo()
    _input = STDSCR.getstr().decode('utf-8-sig')
    curses.noecho()
    STDSCR.erase()
    STDSCR.refresh()

    # TODO check if valid symbol
    try:
        globals.thread_manager.add_thread(run, 'quote_thread')
        globals.keyboard.start_listener(on_press)
    except BaseException as ex:
        print_exc()

def main():
    globals.init()
    STDSCR.addstr(0,0, "Starting Program...")
    outer = ''
    while outer == '':
        if not globals.thread_manager.are_threads_running():
            STDSCR.addstr(0,0, "Press 'n' to view a stock's price or 'exit' to exit program.")
            STDSCR.addstr(1,0, "--> ")
            curses.echo()
            _input = STDSCR.getstr().decode('utf-8-sig')
            curses.noecho()
            STDSCR.erase()
            STDSCR.refresh()

            if _input.lower() == 'exit':
                outer = ''
                break
            elif _input.lower() == 'n':
                start_quote_thread()


def global_except_hook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)

sys.excepthook = global_except_hook

def exit_handler():
    curses_config.tear_down_curses()

atexit.register(exit_handler)

if __name__ == '__main__':
    main()

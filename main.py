import time
import sys
import atexit
import curses
from threading import Thread
from traceback import print_exc
from pynput.keyboard import Listener
from api import FinnhubAPI
from common import API_KEY
from curses_config import CursesConfig
from thread_manager import ThreadManager
from keyboard import Keyboard

curses_config = CursesConfig()
thread_manager = ThreadManager()
STDSCR = curses_config.init_curses()
KEY_LISTEN = False
starttime = time.time()

keyboard = Keyboard()

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

# GLOBAL_THREAD = None
# GLOBAL_THREAD_RUNNING = False
    
def on_press(key):
    global KEY_LISTEN
    # global GLOBAL_THREAD
    # global GLOBAL_THREAD_RUNNING
    try:
        if key.char == 'q':
            keyboard.stop_listener('backspace')
            KEY_LISTEN = True
            # GLOBAL_THREAD_RUNNING = False
            # GLOBAL_THREAD.join()
            thread_manager.join_thread('quote_thread')
            KEY_LISTEN = False
    except AttributeError:
        print_exc()
    except BaseException:
        print_exc()

def start_quote_thread() -> None:
    STDSCR.addstr(0,0, f"Enter stock symbol.\n--> ")
    # c = STDSCR.getkey()
    curses.echo()
    _input = STDSCR.getstr().decode('utf-8-sig')
    curses.noecho()
    STDSCR.erase()
    STDSCR.refresh()

    # TODO check if valid symbol
    try:
        # GLOBAL_THREAD = Thread(target=run, name='quote_thread', args=(lambda: KEY_LISTEN,))
        # GLOBAL_THREAD.start()
        # GLOBAL_THREAD_RUNNING = True
        thread_manager.add_thread(run, 'quote_thread', KEY_LISTEN)
        keyboard.start_listener(on_press)
    except BaseException as ex:
        print_exc()

def main():
    STDSCR.addstr(0,0, "Starting Program...")
    outer = ''
    while outer == '':
        if not thread_manager.are_threads_running():
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


    # finnhub_api = FinnhubAPI(API_KEY) f
    # response = finnhub_api.get_quote('amd')
    # print(response)

def global_except_hook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)

sys.excepthook = global_except_hook

def exit_handler():
    curses_config.tear_down_curses()

atexit.register(exit_handler)

if __name__ == '__main__':
    main()

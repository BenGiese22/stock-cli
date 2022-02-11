import time 
import curses
import atexit
from threading import Thread
from traceback import print_exc
from pynput.keyboard import Listener
from api import FinnhubAPI
from common import API_KEY
from curses_config import CursesConfig

curses_config = CursesConfig()
STDSCR = curses_config.init_curses()
KEY_LISTEN = False
starttime = time.time()

def run(key_listen):
    try:
        x = 0
        while True:
            STDSCR.addstr(0, 0, f"hit - {x}", curses_config.get_green_color_pair())
            time.sleep(1.00 - ((time.time() - starttime) % 1.00))
            STDSCR.refresh()
            x += 1
            if key_listen():
                break
    except BaseException as ex:
        print_exc()

GLOBAL_THREAD = Thread(target=run, args=(lambda: KEY_LISTEN,))
    
def on_press(key):
    global KEY_LISTEN
    global GLOBAL_THREAD
    try:
        if key.char == 'q':
            KEY_LISTEN = True
            GLOBAL_THREAD.join()
            print('thread killed')
    except AttributeError:
        print(key)

def main():
    
    global GLOBAL_THREAD
    GLOBAL_THREAD.start()

    listener = Listener(
        on_press=on_press
    )
    listener.start()
    # finnhub_api = FinnhubAPI(API_KEY)
    # response = finnhub_api.get_quote('amd')
    # print(response)

def exit_handler():
    curses_config.tear_down_curses()

atexit.register(exit_handler)

if __name__ == '__main__':
    main()

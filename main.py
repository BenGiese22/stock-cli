import time
import sys
import atexit
import curses
import globals
from traceback import print_exc
from api import FinnhubAPI
from common import API_KEY


# curses_config = CursesConfig()
# thread_manager = ThreadManager()
# globals.STDSCR = curses_config.init_curses()
# KEY_LISTEN = False
starttime = time.time()

# keyboard = Keyboard()

# TODO write low opacity press q to exit?
def run(key_listen):
    curses.curs_set(0)
    try:
        x = 0
        while True:
            globals.STDSCR.addstr(3, 0, f"hit - {x} - {key_listen} - {type(key_listen)}", globals.curses_config.get_green_color_pair())
            time.sleep(1.00 - ((time.time() - starttime) % 1.00))
            globals.STDSCR.refresh()
            x += 1
            if key_listen():
                print('key listen hit xxxxxx ------')
                curses.curs_set(1)
                break
    except BaseException as ex:
        print_exc()

# GLOBAL_THREAD = None
# GLOBAL_THREAD_RUNNING = False
    
def on_press(key):
    # global GLOBAL_THREAD
    # global GLOBAL_THREAD_RUNNING
    try:
        if key.char == 'q':
            print('attempting stop')
            globals.keyboard.stop_listener('backspace')
            globals.KEY_LISTEN = True
            # GLOBAL_THREAD_RUNNING = False
            # GLOBAL_THREAD.join()
            time.sleep(2)
            globals.thread_manager.join_thread('quote_thread')
            globals.KEY_LISTEN = False
    except AttributeError:
        print_exc()
    except BaseException:
        print_exc()

def start_quote_thread() -> None:
    globals.STDSCR.addstr(0,0, f"Enter stock symbol.\n--> ")
    # c = globals.STDSCR.getkey()
    curses.echo()
    _input = globals.STDSCR.getstr().decode('utf-8-sig')
    curses.noecho()
    globals.STDSCR.erase()
    globals.STDSCR.refresh()

    # TODO check if valid symbol
    try:
        # GLOBAL_THREAD = Thread(target=run, name='quote_thread', args=(lambda: KEY_LISTEN,))
        # GLOBAL_THREAD.start()
        # GLOBAL_THREAD_RUNNING = True
        globals.thread_manager.add_thread(run, 'quote_thread')
        globals.keyboard.start_listener(on_press)
    except BaseException as ex:
        print_exc()

def main():
    globals.init()
    globals.STDSCR.addstr(0,0, "Starting Program...")
    outer = ''
    while outer == '':
        if not globals.thread_manager.are_threads_running():
            globals.STDSCR.addstr(0,0, "Press 'n' to view a stock's price or 'exit' to exit program.")
            globals.STDSCR.addstr(1,0, "--> ")
            curses.echo()
            _input = globals.STDSCR.getstr().decode('utf-8-sig')
            curses.noecho()
            globals.STDSCR.erase()
            globals.STDSCR.refresh()

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
    globals.curses_config.tear_down_curses()

atexit.register(exit_handler)

if __name__ == '__main__':
    main()

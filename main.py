from pickle import GLOBAL
from threading import Thread
from pynput.keyboard import Listener
import time 
# import sys
import curses
import atexit
from api import FinnhubAPI
"""
Request API Key on init load. Validate it. Store it for continous use. 

Graphing Commands, see on-going stock information.
- Commands to view different time frames - 1d (xd) 1w (xw) 1m (xm) 1y (xy)
- Possible Libraries
    - plotext
    - termplotlib
    - uniplot
    - termplot
    - terminalplot

Colored text - use "Colorama"

sys.stdout.write("\rDoing thing %i" % i)
sys.stdout.flush()
"""

DEBUG = True


if DEBUG:
    API_KEY = 'sandbox_c837q2qad3ift3bm38e0'
else:
    API_KEY = 'c837q2qad3ift3bm38dg'

KEY_LISTEN = False
starttime = time.time()

def run(key_listen):
    #Timer goes here
    # print('hit')
    x = 0
    while True:
        # sys.stdout.write(f"hit - {x}\n\r")

        time.sleep(1.00 - ((time.time() - starttime) % 1.00))
        sys.stdout.flush()
        x += 1
        if key_listen():
            break

GLOBAL_THREAD = Thread(target=run, args=(lambda: KEY_LISTEN,))
    
def on_press(key):
    global KEY_LISTEN
    global GLOBAL_THREAD
    try:
        # print(key.char)
        if key.char == 'q':
            KEY_LISTEN = True
            GLOBAL_THREAD.join()
            print('thread killed')
    except AttributeError:
        print(key)

def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    
    # t1 = Thread(target = run, args =(lambda : KEY_LISTEN, ))
    # t1 = Thread(target=run, args=(lambda: KEY_LISTEN))
    # t1.start()
    global GLOBAL_THREAD
    GLOBAL_THREAD.start()
    # time.sleep(10)
    # x = input()
    # print(x)
    # KEY_LISTEN = False

    listener = Listener(
        on_press=on_press
    )
    listener.start()
    # time.sleep(10)
    # KEY_LISTEN = False

    # print('hit')
    # t1.join()
    # print('thread killed')
    # Thread(target = timer).start()
    # input("Press enter to stop")
    # user_input = ''
    # print("Press 'q' to stop.")
    # while user_input != 'q':
    #     user_input = readchar.readchar()
    #     print(user_input)
    # print('done')
    
    # finnhub_api = FinnhubAPI(API_KEY)
    # response = finnhub_api.get_quote('amd')
    # print(response)

def exit_handler():
    curses.nocbreak()
    curses.echo()
    curses.endwin()

if __name__ == '__main__':
    main()

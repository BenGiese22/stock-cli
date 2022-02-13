# import time
import curses
# from traceback import print_exc
from api import FinnhubAPI
# from curses_config import CursesConfig

from event_handler import EventHandler
# from thread_manager import ThreadManager
# from keyboard_controller import Keyboard

# thread_manager = ThreadManager()
# # keyboard = Keyboard()
# curses_config = CursesConfig()
# STDSCR = curses_config.init_window()
# starttime = time.time()

# # TODO write low opacity press q to exit?
# def run_quote(key_listen):
#     curses.curs_set(0)
#     try:
#         x = 0
#         while True:
#             STDSCR.addstr(0, 0, f"hit - {x}", curses_config.get_green_color_pair())
#             time.sleep(1.00 - ((time.time() - starttime) % 1.00))
#             STDSCR.refresh()
#             x += 1
#             if key_listen():
#                 curses.curs_set(1)
#                 break
#     except BaseException as ex:
#         print_exc()

    
# def quit_quote(key):
#     try:
#         if key.char == 'q':
#             keyboard.stop_listener('backspace')
#             thread_manager.join_thread('quote_thread')
#     except AttributeError:
#         print_exc()
#     except BaseException:
#         print_exc()

# def start_quote_thread() -> None:
#     STDSCR.addstr(0,0, f"Enter stock symbol.\n--> ")
#     curses.echo()
#     _input = STDSCR.getstr().decode('utf-8-sig')
#     curses.noecho()
#     STDSCR.erase()
#     STDSCR.refresh()

#     # TODO check if valid symbol
#     try:
#         thread_manager.add_thread(run_quote, 'quote_thread')
#         keyboard.start_listener(quit_quote)
#     except BaseException as ex:
#         print_exc()


def run_cli():
    event_handler = EventHandler()
    # STDSCR.addstr(0,0, "Starting Program...")
    outer = ''
    while outer == '':
        if not event_handler.event_running():
            _input = event_handler.get_master_input()

            if _input.lower() == 'exit':
                outer = ''
                break
            elif _input.lower() == 'n':
                event_handler.start_quote()

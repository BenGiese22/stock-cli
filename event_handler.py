import time
from thread_manager import ThreadManager
from keyboard_controller import KeyboardController
from curses_config import CursesConfig

from traceback import print_exc

class EventHandler():

    def __init__(self):
        self.thread_manager = ThreadManager()
        self.keyboard_controller = KeyboardController()
        self.curses_config = CursesConfig()
        self.window = self.curses_config.init_window()
        self.starttime = time.time()

    def get_master_input(self) -> str:
        self.window.addstr(0,0, "Press 'n' to view a stock's price or 'exit' to exit program.")
        self.window.addstr(1,0, "--> ")
        self.curses_config.echo()
        _input = self.window.getstr().decode('utf-8-sig')
        self.curses_config.noecho()
        self.window.erase()
        self.window.refresh()
        return _input

    def start_quote(self) -> None:
        self.window.addstr(0,0, f"Enter stock symbol.\n--> ")
        self.curses_config.echo()
        _input = self.window.getstr().decode('utf-8-sig')
        self.curses_config.noecho()
        self.window.erase()
        self.window.refresh()

        # TODO check if valid symbol
        try:
            self.thread_manager.add_thread(self.run_quote, 'quote_thread', _input)
            self.keyboard_controller.start_listener(self.quit_quote)
        except BaseException as ex:
            print_exc()


    def quit_quote(self, key):
        try:
            if key.char == 'q':
                self.keyboard_controller.stop_listener('backspace')
                self.thread_manager.join_thread('quote_thread')
        except AttributeError:
            print_exc()
        except BaseException:
            print_exc()

    def run_quote(self, key_listen, stock_symbol):
        self.curses_config.set_cursor(0)
        try:
            x = 0
            while True:
                self.window.addstr(0, 0, f"hit - {x} - {stock_symbol}", self.curses_config.get_green_color_pair())
                time.sleep(1.00 - ((time.time() - self.starttime) % 1.00))
                self.window.refresh()
                x += 1
                if key_listen():
                    self.curses_config.set_cursor(1)
                    break
        except BaseException as ex:
            print_exc()

    def event_running(self) -> bool:
        return self.thread_manager.are_threads_running()

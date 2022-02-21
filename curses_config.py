import curses
from enum import Enum

class ColorMapping(Enum):
    GREEN = 1
    RED = 2

class InvalidCursorError(RuntimeError):
    pass

class CursesConfig:

    def __init__(self) -> None:
        pass

    def init_window(self) -> None:
        stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.noecho()
        curses.cbreak()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_WHITE)
        self.set_cursor(0)
        return stdscr

    @staticmethod
    def tear_down_curses() -> None:
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def get_green_color_pair(self) -> int:
        return curses.color_pair(ColorMapping.GREEN.value)

    def get_red_color_pair(self) -> int:
        return curses.color_pair(ColorMapping.RED.value)

    def set_cursor(self, desired_cursor_value: int) -> None:
        if (desired_cursor_value > 2) or (desired_cursor_value < 0):
            raise InvalidCursorError("Cursor values options are 0, 1, or 2.")
        curses.curs_set(desired_cursor_value)

    def echo(self) -> None:
        curses.echo()

    def noecho(self) -> None:
        curses.noecho()

    def disable(self) -> None:
        curses.endwin()

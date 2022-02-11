import curses
from enum import Enum

class ColorMapping(Enum):
    GREEN = 1
    RED = 2

class CursesConfig:

    def __init__(self) -> None:
        pass
        
    def init_curses(self) -> None:
        stdscr = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.noecho()
        curses.cbreak()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        return stdscr

    def tear_down_curses(self) -> None:
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def get_green_color_pair(self) -> int:
        return curses.color_pair(ColorMapping.GREEN.value)

    def get_red_color_pair(self) -> int:
        return curses.color_pair(ColorMapping.RED.value)

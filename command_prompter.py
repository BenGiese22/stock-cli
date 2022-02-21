import sys
import tty
import termios
from curses_config import CursesConfig
from events.event import Event
from enums.keys import Keys


class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setcbreak(sys.stdin.fileno())
                tty.setraw(sys.stdin.fileno())
                first_char = sys.stdin.read(1)
                if first_char == '\x1b':
                    second_and_third_chars = sys.stdin.read(2)
                    return first_char + second_and_third_chars
                return first_char
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


class CommandPrompter:

    def __init__(self) -> None:
        self.curses_config = CursesConfig()
        self.window = self.curses_config.init_window()
        self.commands = ['a','b','c']

    def prompt_user(self) -> None:
        inkey = _Getch()
        command_selected = 0
        self._print_commands(command_selected)
        k = ''
        while k not in (Keys.Q.value, Keys.ENTER.value):
            k = inkey()
            if k == Keys.UP.value:
                command_selected -= 1
            elif k == Keys.DOWN.value:
                command_selected += 1
            self._print_commands(command_selected)
        return command_selected

    def _print_commands(self, command_selected: int) -> None:
        self.window.erase()
        for index, command in enumerate(self.commands):
            if index == command_selected:
                self.window.addstr(index, 0, command, self.curses_config.get_cyan_color_pair())
            else:
                self.window.addstr(index, 0, command)
        self.window.refresh()



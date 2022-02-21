import sys
import tty
import termios
from curses_config import CursesConfig
from enums.keys import Keys

from events.base_event import BaseEvent
from events.watchlist_event import WatchlistEvent
from events.graph_event import GraphEvent


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


# Make this into the cli
class CommandPrompter:

    def __init__(self) -> None:
        self.curses_config = CursesConfig()
        self.window = self.curses_config.init_window()

        self.base_event = BaseEvent()
        self.watchlist_event = WatchlistEvent()
        self.graph_event = GraphEvent()
        self.commands = self._init_commands()

    def run_cli(self):
        while(1):
            event_running = self.base_event.is_master_thread()
            if not event_running:
                command_selected = self.prompt_user()
                command_func = self.commands[command_selected]['command_func']
                command_func()

    def prompt_user(self) -> None:
        inkey = _Getch()
        command_selected = 0
        self._print_commands(command_selected)
        k = ''
        while k not in (Keys.Q.value, Keys.ENTER.value):
            k = inkey()
            command_selected = self._handle_key_press(command_selected, k)
            self._print_commands(command_selected)
        return command_selected

    def _handle_key_press(self, current_selected: int, k: str) -> int:
        if k == Keys.UP.value:
            to_be = current_selected - 1
            if to_be < 0:
                return current_selected
            elif self.commands[to_be] == '':
                return to_be - 1
            else:
                return to_be
        elif k == Keys.DOWN.value:
            to_be = current_selected + 1
            if to_be > len(self.commands):
                return current_selected
            elif self.commands[to_be] == '':
                return to_be + 1
            else:
                return to_be
        return current_selected

    def _print_commands(self, command_selected: int) -> None:
        self.window.erase()
        for index, command in enumerate(self.commands):
            if command == '':
                continue
            if index == command_selected:
                self.window.addstr(index, 0, command['command_name'], self.curses_config.get_cyan_color_pair())
            else:
                self.window.addstr(index, 0, command['command_name'])
        self.window.refresh()

    # def _print_commands(self, command_selected: int) -> None:
    #     self.window.erase()
    #     line_index = 0
    #     for command_group in self.commands:
    #         commands = self.commands[command_group]
            


    def _init_commands(self) -> list:
        commands = []
        # commands.extend(self.watchlist_event.get_commands())
        # commands.extend(self.event.get_commands())
        commands.extend(self.watchlist_event.get_commands())
        commands.append('')
        commands.extend(self.base_event.get_commands())
        return commands


import atexit
import sys
from command_prompter import CommandPrompter
from curses_config import CursesConfig

def main():
    command_prompter = CommandPrompter()
    command_prompter.run_cli()


def global_except_hook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)

sys.excepthook = global_except_hook

atexit.register(CursesConfig.tear_down_curses)

if __name__ == '__main__':
    main()

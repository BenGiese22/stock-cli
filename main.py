import cli
import atexit
import sys
from curses_config import CursesConfig

def main():
    cli.run_cli()


def global_except_hook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)

sys.excepthook = global_except_hook

atexit.register(CursesConfig.tear_down_curses)

if __name__ == '__main__':
    main()

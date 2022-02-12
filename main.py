import cli
import atexit
import sys

def main():
    cli.run_quote()


def global_except_hook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)

sys.excepthook = global_except_hook

atexit.register(cli.exit_handler)

if __name__ == '__main__':
    main()

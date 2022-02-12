from thread_manager import ThreadManager
from keyboard import Keyboard


def init() -> None:
    global thread_manager
    global KEY_LISTENER_HIT
    global keyboard
    thread_manager = ThreadManager()
    KEY_LISTENER_HIT = False
    keyboard = Keyboard()


import globals
from pynput.keyboard import Listener, Key, Controller

class Keyboard():

    def __init__(self) -> None:
        self.listener = None
        self.controller = Controller()

    def start_listener(self, _on_press_func) -> None:
        globals.KEY_LISTENER_HIT = False
        self.listener = Listener(
            on_press=_on_press_func
        )
        self.listener.start()

    def stop_listener(self, key_press: str) -> None:
        globals.KEY_LISTENER_HIT = True
        if self.listener:
            self.controller.press(Key.backspace)
            self.listener.stop()
            

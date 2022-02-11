from pynput.keyboard import Listener, Key, Controller

class Keyboard():

    def __init__(self) -> None:
        self.listener = None
        self.controller = Controller()

    def start_listener(self, _on_press_func) -> None:
        self.listener = Listener(
            on_press=_on_press_func
        )
        self.listener.start()

    def stop_listener(self, key_press: str) -> None:
        if self.listener:
            self.controller.press(Key.backspace)
            self.listener.stop()
            

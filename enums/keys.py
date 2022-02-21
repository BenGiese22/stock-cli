from enum import Enum

class Keys(Enum):
    UP = '\x1b[A'
    DOWN = '\x1b[B'
    LEFT = '\x1b[D'
    RIGHT = '\x1b[C'
    Q = 'q'
    ENTER = '\r'

from enum import Enum

class Move(Enum):
    FOREWORD = "foreword"
    BACKWORD = "backword"
    LEFT = "left"
    RIGHT = "right"
    STOP = "stop"
    DEFAULT = ""
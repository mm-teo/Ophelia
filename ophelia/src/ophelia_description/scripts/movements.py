#!/usr/bin/env python

from enum import Enum

class Comand(Enum):
    FOREWORD = "foreword"
    BACKWORD = "backword"
    LEFT = "left"
    RIGHT = "right"
    STOP = "stop"
    DEFAULT = ""
    SWITCH_MODE = "switch_mode"
#!/usr/bin/env python

from enum import Enum


class Command(Enum):
    FOREWARD = 'foreward'
    BACKWARD = 'backward'
    LEFT = 'left'
    RIGHT = 'right'
    STOP = 'stop'
    DEFAULT = ''
    SWITCH_MODE = 'switch_mode'

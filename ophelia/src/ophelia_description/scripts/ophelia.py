#! /usr/bin/env python

import rospy
from std_msgs.msg import String

import os
import time
from ctypes import CDLL, c_float, Structure, c_int, \
    pointer as pt, \
    POINTER as PT

from movements import Command


class Coordinates(Structure):
    _fields_ = [('firstStep', PT(c_int)),
                ('x', PT(c_float)), ('y', PT(c_float)),
                ('x1', PT(c_float)), ('y1', PT(c_float)), ('z1', PT(c_float)),
                ('x2', PT(c_float)), ('y2', PT(c_float)), ('z2', PT(c_float)),
                ('z', PT(c_float)), ('z3', PT(c_float))
                ]


class Movement:
    __slots__ = 'old_cmd', 'x', 'y', 'z', \
                'x1', 'x2', 'y1', 'y2', 'z1', 'z2', \
                'first_step', \
                'c_alza', 'c_avanti', 'c_avanti_uscita' \
                'c_indietro', 'c_indietro_uscita', \
                'c_ruota_destra', 'c_ruota_destra_uscita', \
                'c_ruota_sinistra', 'c_ruota_sinistra_uscita'

    def __init__(self, x=135.0, y=0.0, z=-31.0, first_step=1):
        self.old_cmd = Command.DEFAULT
        self.x, self.x1, self.x2 = (x, x, x)
        self.y, self.y1, self.y2 = (y, y, y)
        self.z, self.z1, self.z2, self.z3 = (z, z, z, z)
        self.first_step = first_step
        self.c_alza = hexapode_lib.alza
        self.c_avanti = hexapode_lib.avanti
        self.c_avanti_uscita = hexapode_lib.avantiUscita
        self.c_indietro = hexapode_lib.indietro
        self.c_indietro_uscita = hexapode_lib.indietroUscita
        self.c_ruota_destra = hexapode_lib.destra
        self.c_ruota_destra_uscita = hexapode_lib.destraUscita
        self.c_ruota_sinistra = hexapode_lib.sinistra
        self.c_ruota_sinistra_uscita = hexapode_lib.sinistraUscita

    def get_coord(self):
        return Coordinates(
            pt(c_int(self.first_step)),
            pt(c_float(self.x)), pt(c_float(self.y)),
            pt(c_float(self.x1)), pt(c_float(self.y1)), pt(c_float(self.z1)),
            pt(c_float(self.x2)), pt(c_float(self.y2)), pt(c_float(self.z2)),
            pt(c_float(self.z)), pt(c_float(self.z3)))

    def set_coord(self, new_coord):
        self.first_step = new_coord.firstStep.contents.value
        self.x = new_coord.x.contents.value
        self.y = new_coord.y.contents.value
        self.x1 = new_coord.x1.contents.value
        self.y1 = new_coord.y1.contents.value
        self.z1 = new_coord.z1.contents.value
        self.x2 = new_coord.x2.contents.value
        self.y2 = new_coord.y2.contents.value
        self.z2 = new_coord.z2.contents.value
        self.z = new_coord.z.contents.value
        self.z3 = new_coord.z3.contents.value

    def alza(self):
        coord = self.get_coord()
        self.c_alza(coord)
        self.set_coord(coord)

    def avanti(self):
        coord = self.get_coord()
        self.c_avanti(coord)
        self.set_coord(coord)

    def avantiUscita(self):
        coord = self.get_coord()
        self.c_avanti_uscita(coord)
        self.set_coord(coord)

    def indietro(self):
        coord = self.get_coord()
        self.c_indietro(coord)
        self.set_coord(coord)

    def indietroUscita(self):
        coord = self.get_coord()
        self.c_indietro_uscita(coord)
        self.set_coord(coord)

    def ruotaDestra(self):
        coord = self.get_coord()
        self.c_ruota_destra(coord)
        self.set_coord(coord)

    def ruotaDestraUscita(self):
        coord = self.get_coord()
        self.c_ruota_destra_uscita(coord)
        self.set_coord(coord)

    def ruotaSinistra(self):
        coord = self.get_coord()
        self.c_ruota_sinistra(coord)
        self.set_coord(coord)

    def ruotaSinistraUscita(self):
        coord = self.get_coord()
        self.c_ruota_sinistra_uscita(coord)
        self.set_coord(coord)

    def to_default_position(self):
        if self.old_cmd == Command.BACKWARD:
            self.indietroUscita()
        elif self.old_cmd == Command.FOREWARD:
            self.avantiUscita()
        elif self.old_cmd == Command.LEFT:
            self.ruotaSinistraUscita()
        elif self.old_cmd == Command.RIGHT:
            self.ruotaDestraUscita()
        self.old_cmd = Command.DEFAULT

    def control_movement(self, command, move):
        if self.old_cmd == command or self.old_cmd == Command.DEFAULT:
            move()
            self.old_cmd = command
        else:
            self.to_default_position()


def process_command(movement):
    command = Command(movement.data)
    if command == Command.FOREWARD:
        robot.control_movement(command, robot.avanti)
    elif command == Command.BACKWARD:
        robot.control_movement(command, robot.indietro)
    elif command == Command.LEFT:
        robot.control_movement(command, robot.ruotaSinistra)
    elif command == Command.RIGHT:
        robot.control_movement(command, robot.ruotaDestra)
    elif command == Command.STOP:
        if robot.old_cmd == command or robot.old_cmd == Command.DEFAULT:
            robot.old_cmd = Command.DEFAULT
        else:
            robot.to_default_position()


lib_path = os.environ['HEXALIB_PATH']
hexapode_lib = CDLL(lib_path)
if __name__ == '__main__':
    hexapode_lib.initPublisher()
    rospy.init_node('joint_state_interface')

    robot = Movement()
    time.sleep(0.1)  # Necessary: Cpp too fast
    robot.alza()

    rospy.Subscriber(name='/discrete_movement',
                     data_class=String,
                     callback=process_command,
                     queue_size=1)

    rospy.spin()
    hexapode_lib.shutdownPublisher()

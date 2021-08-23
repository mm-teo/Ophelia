#! /usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header, String

import os
import math
import time
from ctypes import CDLL, c_float, Structure, c_int, \
    pointer as pt, \
    POINTER as PT

from traiettoria import Cinematica
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
                'c_alza', 'c_avanti', 'c_avanti_uscita'

    def __init__(self, x=135.0, y=0.0, z=-31.0, first_step=1):
        self.old_cmd = Command.DEFAULT
        self.x = x
        self.x1 = x
        self.x2 = x
        self.y = y
        self.y1 = y
        self.y2 = y
        self.z = z
        self.z1 = z
        self.z2 = z
        self.z3 = z
        self.first_step = first_step
        self.c_alza = hexapode_lib.alza
        self.c_avanti = hexapode_lib.avanti
        self.c_avanti_uscita = hexapode_lib.avantiUscita

    move = JointState()
    braccio1 = Cinematica()

    def get_coord(self):
        return Coordinates(
            pt(c_int(self.first_step)),
            pt(c_float(self.x)), pt(c_float(self.y)),
            pt(c_float(self.x1)), pt(c_float(self.y1)), pt(c_float(self.z1)),
            pt(c_float(self.x2)), pt(c_float(self.y2)), pt(c_float(self.z2)),
            pt(c_float(self.z)), pt(c_float(self.z3)))

    def set_coord(self, new_coord):
        print(new_coord.firstStep.contents.value)
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
        Movement.z3 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z3 < -100:
                # d=right a=coxa, f=femur, t=tibia
                Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, -Movement.y, Movement.z3)
                Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, -Movement.y, Movement.z3)
                Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, -Movement.y, Movement.z3)

                Movement.sx_a_1 = Movement.dx_a_2
                Movement.sx_f_1 = -Movement.dx_f_2
                Movement.sx_t_1 = -Movement.dx_t_2

                Movement.sx_a_3 = Movement.dx_a_2
                Movement.sx_f_3 = -Movement.dx_f_2
                Movement.sx_t_3 = -Movement.dx_t_2

                self.moving()
                Movement.z3 = Movement.z3+1
                self.pubb()

        Movement.firstStep = 0
        Movement.z1 = Movement.z3
        Movement.z2 = Movement.z3

        while Movement.y > -40:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, Movement.y1, Movement.z)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x2, Movement.y1, Movement.z2)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x2, Movement.y1, Movement.z2)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x2, Movement.y1, Movement.z2)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x, -Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, -Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, -Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, Movement.y1, Movement.z2)

            self.moving()
            Movement.y = Movement.y-1
            Movement.x1 = Movement.x1+(1/math.sqrt(2))
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.01875+100)
            Movement.z2 = -0.0375*math.pow(Movement.x1-135, 2)-100
            self.pubb()

        while Movement.y < 40:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, Movement.y1, Movement.z2)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x2, Movement.y1, Movement.z)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x2, Movement.y1, Movement.z)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x2, Movement.y1, Movement.z)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x, -Movement.y, Movement.z1)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, -Movement.y, Movement.z1)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, -Movement.y, Movement.z1)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, Movement.y1, Movement.z)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, Movement.y1, Movement.z)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, Movement.y1, Movement.z)

            self.moving()
            Movement.y = Movement.y+1
            Movement.x1 = Movement.x1-(1/math.sqrt(2))
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.01875+100)
            Movement.z2 = -0.0375*math.pow(Movement.x1-135, 2)-100
            self.pubb()

    def indietroUscita(self):
        Movement.firstStep = 1
        while Movement.y > 0:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, Movement.y1, Movement.z)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x2, Movement.y1, Movement.z2)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x2, Movement.y1, Movement.z2)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x2, Movement.y1, Movement.z2)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x, -Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, -Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, -Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, Movement.y1, Movement.z2)

            self.moving()
            Movement.y = Movement.y-1
            Movement.x1 = Movement.x1+(1/math.sqrt(2))
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.01875+100)
            Movement.z2 = -0.0375*math.pow(Movement.x1-135, 2)-100
            self.pubb()

        while Movement.z2 > -130:
            # d=right a=coxa, f=femur, t=tibia
            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z2)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z2)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z2)

            Movement.sx_a_1 = Movement.dx_a_2
            Movement.sx_f_1 = -Movement.dx_f_2
            Movement.sx_t_1 = -Movement.dx_t_2

            Movement.sx_a_3 = Movement.dx_a_2
            Movement.sx_f_3 = -Movement.dx_f_2
            Movement.sx_t_3 = -Movement.dx_t_2

            self.moving()
            Movement.z2 = Movement.z2-1
            self.pubb()

    def destra(self):
        Movement.z3 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z3 < -100:
                # d=right a=coxa, f=femur, t=tibia
                Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z3)
                Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z3)
                Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z3)

                Movement.sx_a_1 = Movement.dx_a_2
                Movement.sx_f_1 = -Movement.dx_f_2
                Movement.sx_t_1 = -Movement.dx_t_2

                Movement.sx_a_3 = Movement.dx_a_2
                Movement.sx_f_3 = -Movement.dx_f_2
                Movement.sx_t_3 = -Movement.dx_t_2

                self.moving()
                Movement.z3 = Movement.z3+1
                self.pubb()

        Movement.firstStep = 0
        Movement.z1 = Movement.z3
        Movement.z2 = Movement.z3

        while Movement.x > 95:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z1)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, Movement.y1, Movement.z1)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, Movement.y1, Movement.z1)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x1, -Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x1, -Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x1, -Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, -Movement.y1, Movement.z1)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, -Movement.y1, Movement.z1)

            self.moving()
            Movement.x = Movement.x-1
            Movement.x1 = Movement.x1+1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = Movement.y1-(1/math.sqrt(2))
            self.pubb()

        while Movement.x < 175:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z1)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z1)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, -Movement.y1, Movement.z1)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z1)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z1)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, Movement.y1, Movement.z)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, Movement.y1, Movement.z)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x1, Movement.y, Movement.z1)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x1, Movement.y, Movement.z1)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x1, Movement.y, Movement.z1)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, -Movement.y1, Movement.z)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, -Movement.y1, Movement.z)

            self.moving()
            Movement.x = Movement.x+1
            Movement.x1 = Movement.x1-1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = Movement.y1+(1/math.sqrt(2))
            self.pubb()

    def destraUscita(self):
        while Movement.x > 135:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z1)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, Movement.y1, Movement.z1)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, Movement.y1, Movement.z1)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x1, -Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x1, -Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x1, -Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, -Movement.y1, Movement.z1)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, -Movement.y1, Movement.z1)

            self.moving()
            Movement.x = Movement.x-1
            Movement.x1 = Movement.x1+1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = Movement.y1-(1/math.sqrt(2))
            self.pubb()

        while Movement.z2 > -130:
            # d=right a=coxa, f=femur, t=tibia
            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z2)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z2)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z2)

            Movement.sx_a_1 = Movement.dx_a_2
            Movement.sx_f_1 = -Movement.dx_f_2
            Movement.sx_t_1 = -Movement.dx_t_2

            Movement.sx_a_3 = Movement.dx_a_2
            Movement.sx_f_3 = -Movement.dx_f_2
            Movement.sx_t_3 = -Movement.dx_t_2

            self.moving()
            Movement.z2 = Movement.z2-1
            self.pubb()

    def sinistra(self):
        Movement.z3 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z3 < -100:
                # d=right a=coxa, f=femur, t=tibia
                Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z3)
                Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z3)
                Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z3)

                Movement.sx_a_1 = Movement.dx_a_2
                Movement.sx_f_1 = -Movement.dx_f_2
                Movement.sx_t_1 = -Movement.dx_t_2

                Movement.sx_a_3 = Movement.dx_a_2
                Movement.sx_f_3 = -Movement.dx_f_2
                Movement.sx_t_3 = -Movement.dx_t_2

                self.moving()
                Movement.z3 = Movement.z3+1
                self.pubb()

        Movement.firstStep = 0
        Movement.z1 = Movement.z3
        Movement.z2 = Movement.z3

        while Movement.x < 175:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z1)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, Movement.y1, Movement.z1)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, Movement.y1, Movement.z1)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x1, -Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x1, -Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x1, -Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, -Movement.y1, Movement.z1)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, -Movement.y1, Movement.z1)

            self.moving()
            Movement.x = Movement.x+1
            Movement.x1 = Movement.x1-1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = Movement.y1+(1/math.sqrt(2))
            self.pubb()

        while Movement.x > 95:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z1)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z1)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, -Movement.y1, Movement.z1)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z1)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z1)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, Movement.y1, Movement.z)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, Movement.y1, Movement.z)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x1, Movement.y, Movement.z1)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x1, Movement.y, Movement.z1)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x1, Movement.y, Movement.z1)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, -Movement.y1, Movement.z)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, -Movement.y1, Movement.z)

            self.moving()
            Movement.x = Movement.x-1
            Movement.x1 = Movement.x1+1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = Movement.y1-(1/math.sqrt(2))
            self.pubb()

    def sinistraUscita(self):
        while Movement.x < 135:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z1)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, Movement.y1, Movement.z1)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, Movement.y1, Movement.z1)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x1, -Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x1, -Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x1, -Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x2, -Movement.y1, Movement.z1)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x2, -Movement.y1, Movement.z1)

            self.moving()
            Movement.x = Movement.x+1
            Movement.x1 = Movement.x1-1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = Movement.y1+(1/math.sqrt(2))
            self.pubb()

        while Movement.z2 > -130:
            # d=right a=coxa, f=femur, t=tibia
            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z2)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z2)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z2)

            Movement.sx_a_1 = Movement.dx_a_2
            Movement.sx_f_1 = -Movement.dx_f_2
            Movement.sx_t_1 = -Movement.dx_t_2

            Movement.sx_a_3 = Movement.dx_a_2
            Movement.sx_f_3 = -Movement.dx_f_2
            Movement.sx_t_3 = -Movement.dx_t_2

            self.moving()
            Movement.z2 = Movement.z2-1
            self.pubb()

    def ruotaDestra(self):
        Movement.z3 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z3 < -80:
                # d=right a=coxa, f=femur, t=tibia
                Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z3)
                Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z3)
                Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z3)

                Movement.dx_a_3 = Movement.dx_a_1
                Movement.dx_f_3 = Movement.dx_f_1
                Movement.dx_t_3 = Movement.dx_t_1

                Movement.sx_a_2 = Movement.dx_a_1
                Movement.sx_f_2 = -Movement.dx_f_1
                Movement.sx_t_2 = -Movement.dx_t_1

                self.moving()
                Movement.z3 = Movement.z3+1
                self.pubb()

        Movement.firstStep = 0
        Movement.z1 = Movement.z3
        Movement.z2 = Movement.z3

        while Movement.y < 52:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, Movement.y1, Movement.z2)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x2, -Movement.y1, Movement.z)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x2, -Movement.y1, Movement.z)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x2, -Movement.y1, Movement.z)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z1)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z1)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z1)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, -Movement.y1, Movement.z)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, -Movement.y1, Movement.z)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, -Movement.y1, Movement.z)

            self.moving()
            Movement.y = Movement.y+1
            Movement.y1 = Movement.y*1.199
            b1 = 134.2
            c1 = -36342+math.pow(Movement.y, 2)
            Movement.x = (-b1+math.sqrt(math.pow(b1, 2)-(4*c1)))/(2)
            Movement.z1 = -0.01849*math.pow(Movement.y, 2)-80
            Movement.z2 = -0.01286*math.pow(Movement.y1, 2)-80
            b2 = 211.2
            c2 = -46656+math.pow(Movement.y1, 2)+33.6*Movement.y1
            Movement.x1 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c2)))/(2)

            c3 = -46656+math.pow(Movement.y1, 2)-33.6*Movement.y1
            Movement.x2 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c3)))/(2)
            self.pubb()

        while Movement.y > -52:
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, Movement.y1, Movement.z)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x2, -Movement.y1, Movement.z2)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x2, -Movement.y1, Movement.z2)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x2, -Movement.y1, Movement.z2)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, -Movement.y1, Movement.z2)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, -Movement.y1, Movement.z2)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, -Movement.y1, Movement.z2)

            self.moving()
            Movement.y = Movement.y-1
            Movement.y1 = Movement.y1-1.199
            b1 = 134.2
            c1 = -36342+math.pow(Movement.y, 2)
            Movement.x = (-b1+math.sqrt(math.pow(b1, 2)-(4*c1)))/(2)
            Movement.z1 = -0.01849*math.pow(Movement.y, 2)-80
            Movement.z2 = -0.01286*math.pow(Movement.y1, 2)-80
            b2 = 211.2
            c2 = -46656+math.pow(Movement.y1, 2)+33.6*Movement.y1
            Movement.x1 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c2)))/(2)
            c3 = -46656+math.pow(Movement.y1, 2)-33.6*Movement.y1
            Movement.x2 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c3)))/(2)
            self.pubb()

    def ruotaDestraUscita(self):
        while Movement.y < 0:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, Movement.y1, Movement.z2)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x2, -Movement.y1, Movement.z)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x2, -Movement.y1, Movement.z)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x2, -Movement.y1, Movement.z)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z1)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z1)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z1)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, -Movement.y1, Movement.z)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, -Movement.y1, Movement.z)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, -Movement.y1, Movement.z)

            self.moving()
            Movement.y = Movement.y+1
            Movement.y1 = Movement.y*1.199
            b1 = 134.2
            c1 = -36342+math.pow(Movement.y, 2)
            Movement.x = (-b1+math.sqrt(math.pow(b1, 2)-(4*c1)))/(2)
            Movement.z1 = -0.01849*math.pow(Movement.y, 2)-80
            Movement.z2 = -0.01286*math.pow(Movement.y1, 2)-80
            b2 = 211.2
            c2 = -46656+math.pow(Movement.y1, 2)+33.6*Movement.y1
            Movement.x1 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c2)))/(2)

            c3 = -46656+math.pow(Movement.y1, 2)-33.6*Movement.y1
            Movement.x2 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c3)))/(2)
            self.pubb()
        while Movement.z2 > -130:
            # d=right a=coxa, f=femur, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z2)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z2)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z2)

            Movement.dx_a_3 = Movement.dx_a_1
            Movement.dx_f_3 = Movement.dx_f_1
            Movement.dx_t_3 = Movement.dx_t_1

            Movement.sx_a_2 = Movement.dx_a_1
            Movement.sx_f_2 = -Movement.dx_f_1
            Movement.sx_t_2 = -Movement.dx_t_1

            self.moving()
            Movement.z2 = Movement.z2-1
            self.pubb()

        Movement.firstStep = 0

    def ruotaSinistra(self):
        Movement.z3 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z3 < -80:
                # d=right a=coxa, f=femur, t=tibia
                Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z3)
                Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z3)
                Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z3)

                Movement.dx_a_3 = Movement.dx_a_1
                Movement.dx_f_3 = Movement.dx_f_1
                Movement.dx_t_3 = Movement.dx_t_1

                Movement.sx_a_2 = Movement.dx_a_1
                Movement.sx_f_2 = -Movement.dx_f_1
                Movement.sx_t_2 = -Movement.dx_t_1

                self.moving()
                Movement.z3 = Movement.z3+1
                self.pubb()

        Movement.firstStep = 0
        Movement.z1 = Movement.z3
        Movement.z2 = Movement.z3

        while Movement.y < 52:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y1, Movement.z2)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y1, Movement.z2)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y1, Movement.z2)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, -Movement.y1, Movement.z2)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z2)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z2)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x2, Movement.y1, Movement.z)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x2, Movement.y1, Movement.z)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x2, Movement.y1, Movement.z)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x, -Movement.y, Movement.z1)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, -Movement.y, Movement.z1)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, -Movement.y, Movement.z1)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, Movement.y1, Movement.z)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, Movement.y1, Movement.z)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, Movement.y1, Movement.z)

            self.moving()
            Movement.y = Movement.y+1
            Movement.y1 = Movement.y*1.199
            b1 = 134.2
            c1 = -36342+math.pow(Movement.y, 2)
            Movement.x = (-b1+math.sqrt(math.pow(b1, 2)-(4*c1)))/(2)
            Movement.z1 = -0.01849*math.pow(Movement.y, 2)-80
            Movement.z2 = -0.01286*math.pow(Movement.y1, 2)-80
            b2 = 211.2
            c2 = -46656+math.pow(Movement.y1, 2)+33.6*Movement.y1
            Movement.x1 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c2)))/(2)

            c3 = -46656+math.pow(Movement.y1, 2)-33.6*Movement.y1
            Movement.x2 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c3)))/(2)
            self.pubb()

        while Movement.y > -52:
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y1, Movement.z)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y1, Movement.z)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y1, Movement.z)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z1)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x2, Movement.y1, Movement.z2)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x2, Movement.y1, Movement.z2)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x2, Movement.y1, Movement.z2)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x, -Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, -Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, -Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, Movement.y1, Movement.z2)

            self.moving()
            Movement.y = Movement.y-1
            Movement.y1 = Movement.y1-1.199
            b1 = 134.2
            c1 = -36342+math.pow(Movement.y, 2)
            Movement.x = (-b1+math.sqrt(math.pow(b1, 2)-(4*c1)))/(2)
            Movement.z1 = -0.01849*math.pow(Movement.y, 2)-80
            Movement.z2 = -0.01286*math.pow(Movement.y1, 2)-80
            b2 = 211.2
            c2 = -46656+math.pow(Movement.y1, 2)+33.6*Movement.y1
            Movement.x1 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c2)))/(2)
            c3 = -46656+math.pow(Movement.y1, 2)-33.6*Movement.y1
            Movement.x2 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c3)))/(2)
            self.pubb()

    def ruotaSinistraUscita(self):
        while Movement.y < 0:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y1, Movement.z2)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y1, Movement.z2)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y1, Movement.z2)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z)

            Movement.dx_a_3 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x2, -Movement.y1, Movement.z2)
            Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z2)
            Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z2)

            Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x2, Movement.y1, Movement.z)
            Movement.sx_f_1 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x2, Movement.y1, Movement.z)
            Movement.sx_t_1 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x2, Movement.y1, Movement.z)

            Movement.sx_a_2 = - \
                Movement.braccio1.calcoloIK_joint1(
                    Movement.x, -Movement.y, Movement.z1)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, -Movement.y, Movement.z1)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, -Movement.y, Movement.z1)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, Movement.y1, Movement.z)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, Movement.y1, Movement.z)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, Movement.y1, Movement.z)

            self.moving()
            Movement.y = Movement.y+1
            Movement.y1 = Movement.y*1.199
            b1 = 134.2
            c1 = -36342+math.pow(Movement.y, 2)
            Movement.x = (-b1+math.sqrt(math.pow(b1, 2)-(4*c1)))/(2)
            Movement.z1 = -0.01849*math.pow(Movement.y, 2)-80
            Movement.z2 = -0.01286*math.pow(Movement.y1, 2)-80
            b2 = 211.2
            c2 = -46656+math.pow(Movement.y1, 2)+33.6*Movement.y1
            Movement.x1 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c2)))/(2)

            c3 = -46656+math.pow(Movement.y1, 2)-33.6*Movement.y1
            Movement.x2 = (-b2+math.sqrt(math.pow(b2, 2)-(4*c3)))/(2)
            self.pubb()
        while Movement.z2 > -130:
            # d=right a=coxa, f=femur, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z2)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z2)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z2)

            Movement.dx_a_3 = Movement.dx_a_1
            Movement.dx_f_3 = Movement.dx_f_1
            Movement.dx_t_3 = Movement.dx_t_1

            Movement.sx_a_2 = Movement.dx_a_1
            Movement.sx_f_2 = -Movement.dx_f_1
            Movement.sx_t_2 = -Movement.dx_t_1

            self.moving()
            Movement.z2 = Movement.z2-1
            self.pubb()

        Movement.firstStep = 0

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

    rospy.Subscriber(name='/keyboard_command',
                     data_class=String,
                     callback=process_command,
                     queue_size=1)

    rospy.spin()
    hexapode_lib.shutdownPublisher()

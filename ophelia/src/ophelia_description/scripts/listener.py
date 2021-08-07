#! /usr/bin/env python

import time
import math
import rospy
from traiettoria import Cinematica
from std_msgs.msg import String
from adafruit_servokit import ServoKit


class Movement:
    def __init__(self):
        pass

    # def posizione base
    x = 135.0
    y = 0.0
    z = -25.0

    wait = 0.001
    step = 4
    braccio1 = Cinematica()
    right = ServoKit(channels=16, address=0x40)
    left = ServoKit(channels=16, address=0x41)

    off_a_dx_1 = 6
    off_a_dx_2 = 16
    off_a_dx_3 = -5
    off_f_dx_1 = 13
    off_f_dx_2 = 23
    off_f_dx_3 = 21
    off_t_dx_1 = -10
    off_t_dx_2 = -10
    off_t_dx_3 = -10

    off_a_sx_1 = 0
    off_a_sx_2 = 7
    off_a_sx_3 = 16
    off_f_sx_1 = -0
    off_f_sx_2 = -20
    off_f_sx_3 = -15
    off_t_sx_1 = 10
    off_t_sx_2 = 10
    off_t_sx_3 = 10

    x1 = x
    x2 = x
    z1 = z
    z2 = z
    y1 = y
    y2 = y

    firstStep = 1
    dataOld = ""
    alzato = 0

    def chiusura(self):
        coxaS = Movement.braccio1.calcoloIK_joint1(135, 0, -25)
        coxaD = 180-coxaS
        femurS = Movement.braccio1.calcoloIK_joint2(135, 0, -25)
        femurD = 180-femurS
        tibiaS = Movement.braccio1.calcoloIK_joint3(135, 0, -25)
        tibiaD = 180-tibiaS

        ad1 = coxaD+Movement.off_a_dx_1
        fd1 = femurD+Movement.off_f_dx_1
        td1 = tibiaD+Movement.off_t_dx_1

        ad2 = coxaD+Movement.off_a_dx_2
        fd2 = femurD+Movement.off_f_dx_2
        td2 = tibiaD+Movement.off_t_dx_2

        ad3 = coxaD+Movement.off_a_dx_3
        fd3 = femurD+Movement.off_f_dx_3
        td3 = tibiaD+Movement.off_t_dx_3

        as1 = coxaS+Movement.off_a_sx_1
        fs1 = femurS+Movement.off_f_sx_1
        ts1 = tibiaS+Movement.off_t_sx_1

        as2 = coxaS+Movement.off_a_sx_2
        fs2 = femurS+Movement.off_f_sx_2
        ts2 = tibiaS+Movement.off_t_sx_2

        as3 = coxaS+Movement.off_a_sx_3
        fs3 = femurS+Movement.off_f_sx_3
        ts3 = tibiaS+Movement.off_t_sx_3

        Movement.right.servo[2].angle = ad1
        Movement.right.servo[1].angle = fd1
        Movement.right.servo[0].angle = td1

        Movement.right.servo[5].angle = ad2
        Movement.right.servo[6].angle = fd2
        Movement.right.servo[7].angle = td2

        Movement.right.servo[13].angle = ad3
        Movement.right.servo[14].angle = fd3
        Movement.right.servo[15].angle = td3

        Movement.left.servo[13].angle = as1
        Movement.left.servo[14].angle = fs1
        Movement.left.servo[15].angle = ts1

        Movement.left.servo[5].angle = as2
        Movement.left.servo[6].angle = fs2
        Movement.left.servo[7].angle = ts2

        Movement.left.servo[2].angle = as3
        Movement.left.servo[1].angle = fs3
        Movement.left.servo[0].angle = ts3

    def alza(self):
        while Movement.z > -130:
            coxaS = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z)
            coxaD = 180-coxaS
            femurS = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z)
            femurD = 180-femurS
            tibiaS = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z)
            tibiaD = 180-tibiaS

            ad1 = coxaD+Movement.off_a_dx_1
            fd1 = femurD+Movement.off_f_dx_1
            td1 = tibiaD+Movement.off_t_dx_1

            ad2 = coxaD+Movement.off_a_dx_2
            fd2 = femurD+Movement.off_f_dx_2
            td2 = tibiaD+Movement.off_t_dx_2

            ad3 = coxaD+Movement.off_a_dx_3
            fd3 = femurD+Movement.off_f_dx_3
            td3 = tibiaD+Movement.off_t_dx_3

            as1 = coxaS+Movement.off_a_sx_1
            fs1 = femurS+Movement.off_f_sx_1
            ts1 = tibiaS+Movement.off_t_sx_1

            as2 = coxaS+Movement.off_a_sx_2
            fs2 = femurS+Movement.off_f_sx_2
            ts2 = tibiaS+Movement.off_t_sx_2

            as3 = coxaS+Movement.off_a_sx_3
            fs3 = femurS+Movement.off_f_sx_3
            ts3 = tibiaS+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.z = Movement.z-Movement.step
            if Movement.z < -130:
                Movement.z = -130
            time.sleep(Movement.wait)

    def abbassa(self):
        while Movement.z < -25:
            coxaS = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z)
            coxaD = 180-coxaS
            femurS = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z)
            femurD = 180-femurS
            tibiaS = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z)
            tibiaD = 180-tibiaS

            ad1 = coxaD+Movement.off_a_dx_1
            fd1 = femurD+Movement.off_f_dx_1
            td1 = tibiaD+Movement.off_t_dx_1

            ad2 = coxaD+Movement.off_a_dx_2
            fd2 = femurD+Movement.off_f_dx_2
            td2 = tibiaD+Movement.off_t_dx_2

            ad3 = coxaD+Movement.off_a_dx_3
            fd3 = femurD+Movement.off_f_dx_3
            td3 = tibiaD+Movement.off_t_dx_3

            as1 = coxaS+Movement.off_a_sx_1
            fs1 = femurS+Movement.off_f_sx_1
            ts1 = tibiaS+Movement.off_t_sx_1

            as2 = coxaS+Movement.off_a_sx_2
            fs2 = femurS+Movement.off_f_sx_2
            ts2 = tibiaS+Movement.off_t_sx_2

            as3 = coxaS+Movement.off_a_sx_3
            fs3 = femurS+Movement.off_f_sx_3
            ts3 = tibiaS+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.z = Movement.z+Movement.step
            if Movement.z > -25:
                Movement.z = -25
            time.sleep(Movement.wait)

    def avanti(self):
        Movement.z3 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z3 < -80:
                coxaS = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z3)
                coxaD = 180-coxaS
                femurS = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z3)
                femurD = 180-femurS
                tibiaS = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z3)
                tibiaD = 180-tibiaS

                ad2 = coxaD+Movement.off_a_dx_2
                fd2 = femurD+Movement.off_f_dx_2
                td2 = tibiaD+Movement.off_t_dx_2

                as1 = coxaS+Movement.off_a_sx_1
                fs1 = femurS+Movement.off_f_sx_1
                ts1 = tibiaS+Movement.off_t_sx_1

                as3 = coxaS+Movement.off_a_sx_3
                fs3 = femurS+Movement.off_f_sx_3
                ts3 = tibiaS+Movement.off_t_sx_3

                Movement.right.servo[5].angle = ad2
                Movement.right.servo[6].angle = fd2
                Movement.right.servo[7].angle = td2

                Movement.left.servo[13].angle = as1
                Movement.left.servo[14].angle = fs1
                Movement.left.servo[15].angle = ts1

                Movement.left.servo[2].angle = as3
                Movement.left.servo[1].angle = fs3
                Movement.left.servo[0].angle = ts3

                Movement.z3 = Movement.z3+Movement.step
                if Movement.z3 > 80:
                    Movement.z3 = 80
                time.sleep(Movement.wait)

        Movement.firstStep = 0
        Movement.z1 = Movement.z3
        Movement.z2 = Movement.z3

        while Movement.y > -50:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y-Movement.step
            if Movement.y < -50:
                Movement.y = -50
            Movement.x1 = Movement.x1-Movement.step*(1/math.sqrt(2))
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.02+80)
            Movement.z2 = -(Movement.y1*Movement.y1*0.0282843+80)
            time.sleep(Movement.wait)

        while Movement.y < 50:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y1, Movement.z)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y1, Movement.z)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y1, Movement.z)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y+Movement.step
            if Movement.y > -50:
                Movement.y = -50
            Movement.x1 = Movement.x1+Movement.step*(1/math.sqrt(2))
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.02+80)
            Movement.z2 = -(Movement.y1*Movement.y1*0.0282843+80)
            time.sleep(Movement.wait)

    def avantiUscita(self):
        Movement.firstStep = 1
        while Movement.y > 0:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y-Movement.step
            if Movement.y < 0:
                Movement.y = 0
            Movement.x1 = Movement.x1-Movement.step*(1/math.sqrt(2))
            Movement.x2 = Movement.x2+Movement.step*(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.02+80)
            Movement.z2 = -(Movement.y1*Movement.y1*0.0282843+80)
            time.sleep(Movement.wait)

        while Movement.z2 > -130:
            coxaS = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z2)
            coxaD = 180-coxaS
            femurS = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z2)
            femurD = 180-femurS
            tibiaS = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z2)
            tibiaD = 180-tibiaS

            ad2 = coxaD+Movement.off_a_dx_2
            fd2 = femurD+Movement.off_f_dx_2
            td2 = tibiaD+Movement.off_t_dx_2

            as1 = coxaS+Movement.off_a_sx_1
            fs1 = femurS+Movement.off_f_sx_1
            ts1 = tibiaS+Movement.off_t_sx_1

            as3 = coxaS+Movement.off_a_sx_3
            fs3 = femurS+Movement.off_f_sx_3
            ts3 = tibiaS+Movement.off_t_sx_3

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.z2 = Movement.z2-Movement.step
            if Movement.z2 < -130:
                Movement.z2 = -513
            time.sleep(Movement.wait)

    def indietro(self):
        Movement.z3 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z3 < -80:
                coxaS = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z3)
                coxaD = 180-coxaS
                femurS = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z3)
                femurD = 180-femurS
                tibiaS = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z3)
                tibiaD = 180-tibiaS

                ad2 = coxaD+Movement.off_a_dx_2
                fd2 = femurD+Movement.off_f_dx_2
                td2 = tibiaD+Movement.off_t_dx_2

                as1 = coxaS+Movement.off_a_sx_1
                fs1 = femurS+Movement.off_f_sx_1
                ts1 = tibiaS+Movement.off_t_sx_1

                as3 = coxaS+Movement.off_a_sx_3
                fs3 = femurS+Movement.off_f_sx_3
                ts3 = tibiaS+Movement.off_t_sx_3

                Movement.right.servo[5].angle = ad2
                Movement.right.servo[6].angle = fd2
                Movement.right.servo[7].angle = td2

                Movement.left.servo[13].angle = as1
                Movement.left.servo[14].angle = fs1
                Movement.left.servo[15].angle = ts1

                Movement.left.servo[2].angle = as3
                Movement.left.servo[1].angle = fs3
                Movement.left.servo[0].angle = ts3

                Movement.z3 = Movement.z3+Movement.step
                if Movement.z3 > -80:
                    Movement.z3 = -80
                time.sleep(Movement.wait)

        Movement.firstStep = 0
        Movement.z1 = Movement.z3
        Movement.z2 = Movement.z3

        while Movement.y > -50:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y-Movement.step
            if Movement.y < -50:
                Movement.y = -50
            Movement.x1 = Movement.x1+Movement.step*(1/math.sqrt(2))
            Movement.x2 = Movement.x2-Movement.step*(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.02+80)
            Movement.z2 = -(Movement.y1*Movement.y1*0.0282843+80)
            time.sleep(Movement.wait)

        while Movement.y < 50:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z1)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z1)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z1)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y1, Movement.z)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y1, Movement.z)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y1, Movement.z)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y+Movement.step
            if Movement.y > 50:
                Movement.y = 50
            Movement.x1 = Movement.x1-Movement.step*(1/math.sqrt(2))
            Movement.x2 = Movement.x2+Movement.step*(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.02+80)
            Movement.z2 = -(Movement.y1*Movement.y1*0.0282843+80)
            time.sleep(Movement.wait)

    def indietroUscita(self):
        Movement.firstStep = 1
        while Movement.y > 0:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z2)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y1, Movement.z2)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y-Movement.step
            if Movement.y < 0:
                Movement.y = 0
            Movement.x1 = Movement.x1+Movement.step*(1/math.sqrt(2))
            Movement.x2 = Movement.x2-Movement.step*(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.02+80)
            Movement.z2 = -(Movement.y1*Movement.y1*0.0282843+80)
            time.sleep(Movement.wait)

        while Movement.z2 > -130:
            coxaS = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z2)
            coxaD = 180-coxaS
            femurS = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z2)
            femurD = 180-femurS
            tibiaS = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z2)
            tibiaD = 180-tibiaS

            ad2 = coxaD+Movement.off_a_dx_2
            fd2 = femurD+Movement.off_f_dx_2
            td2 = tibiaD+Movement.off_t_dx_2

            as1 = coxaS+Movement.off_a_sx_1
            fs1 = femurS+Movement.off_f_sx_1
            ts1 = tibiaS+Movement.off_t_sx_1

            as3 = coxaS+Movement.off_a_sx_3
            fs3 = femurS+Movement.off_f_sx_3
            ts3 = tibiaS+Movement.off_t_sx_3

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.z2 = Movement.z2-Movement.step
            if Movement.z2 < -130:
                Movement.z2 = -130
            time.sleep(Movement.wait)

    def destra(self):
        Movement.z3 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z3 < -80:
                coxaS = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z3)
                coxaD = 180-coxaS
                femurS = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z3)
                femurD = 180-femurS
                tibiaS = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z3)
                tibiaD = 180-tibiaS

                ad2 = coxaD+Movement.off_a_dx_2
                fd2 = femurD+Movement.off_f_dx_2
                td2 = tibiaD+Movement.off_t_dx_2

                as1 = coxaS+Movement.off_a_sx_1
                fs1 = femurS+Movement.off_f_sx_1
                ts1 = tibiaS+Movement.off_t_sx_1

                as3 = coxaS+Movement.off_a_sx_3
                fs3 = femurS+Movement.off_f_sx_3
                ts3 = tibiaS+Movement.off_t_sx_3

                Movement.right.servo[5].angle = ad2
                Movement.right.servo[6].angle = fd2
                Movement.right.servo[7].angle = td2

                Movement.left.servo[13].angle = as1
                Movement.left.servo[14].angle = fs1
                Movement.left.servo[15].angle = ts1

                Movement.left.servo[2].angle = as3
                Movement.left.servo[1].angle = fs3
                Movement.left.servo[0].angle = ts3

                Movement.z3 = Movement.z3+Movement.step
                if Movement.z3 > -80:
                    Movement.z3 = -80
                time.sleep(Movement.wait)

        Movement.firstStep = 0
        Movement.z1 = Movement.z3
        Movement.z2 = Movement.z3

        while Movement.x > 85:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.x = Movement.x-Movement.step
            Movement.x1 = Movement.x1+Movement.step
            Movement.x2 = Movement.x2-Movement.step*(1/math.sqrt(2))
            Movement.y1 = Movement.y1-Movement.step*(1/math.sqrt(2))
            Movement.z1 = -(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
            time.sleep(Movement.wait)

        while Movement.x < 185:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y, Movement.z1)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y, Movement.z1)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y, Movement.z1)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.x = Movement.x+Movement.step
            Movement.x1 = Movement.x1-Movement.step
            Movement.x2 = Movement.x2+Movement.step*(1/math.sqrt(2))
            Movement.y1 = Movement.y1+Movement.step*(1/math.sqrt(2))
            Movement.z1 = -(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
            time.sleep(Movement.wait)

    def destraUscita(self):
        while Movement.x > 135:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.x = Movement.x-Movement.step
            Movement.x1 = Movement.x1+Movement.step
            Movement.x2 = Movement.x2-Movement.step*(1/math.sqrt(2))
            Movement.y1 = Movement.y1-Movement.step*(1/math.sqrt(2))
            Movement.z1 = -(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
            time.sleep(Movement.wait)

        Movement.firstStep = 1

        while Movement.z1 > -130:
            coxaS = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z1)
            coxaD = 180-coxaS
            femurS = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z1)
            femurD = 180-femurS
            tibiaS = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z1)
            tibiaD = 180-tibiaS

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            ad2 = coxaD+Movement.off_a_dx_2
            fd2 = femurD+Movement.off_f_dx_2
            td2 = tibiaD+Movement.off_t_dx_2

            as1 = coxaS+Movement.off_a_sx_1
            fs1 = femurS+Movement.off_f_sx_1
            ts1 = tibiaS+Movement.off_t_sx_1

            as3 = coxaS+Movement.off_a_sx_3
            fs3 = femurS+Movement.off_f_sx_3
            ts3 = tibiaS+Movement.off_t_sx_3

            Movement.z1 = Movement.z1-Movement.step
            time.sleep(Movement.wait)

    def sinistra(self):
        Movement.z3 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z3 < -80:
                coxaS = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z3)
                coxaD = 180-coxaS
                femurS = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z3)
                femurD = 180-femurS
                tibiaS = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z3)
                tibiaD = 180-tibiaS

                ad2 = coxaD+Movement.off_a_dx_2
                fd2 = femurD+Movement.off_f_dx_2
                td2 = tibiaD+Movement.off_t_dx_2

                as1 = coxaS+Movement.off_a_sx_1
                fs1 = femurS+Movement.off_f_sx_1
                ts1 = tibiaS+Movement.off_t_sx_1

                as3 = coxaS+Movement.off_a_sx_3
                fs3 = femurS+Movement.off_f_sx_3
                ts3 = tibiaS+Movement.off_t_sx_3

                Movement.right.servo[5].angle = ad2
                Movement.right.servo[6].angle = fd2
                Movement.right.servo[7].angle = td2
                Movement.left.servo[13].angle = as1
                Movement.left.servo[14].angle = fs1
                Movement.left.servo[15].angle = ts1

                Movement.left.servo[2].angle = as3
                Movement.left.servo[1].angle = fs3
                Movement.left.servo[0].angle = ts3

                Movement.z3 = Movement.z3+Movement.step
                time.sleep(Movement.wait)

        Movement.firstStep = 0
        Movement.z1 = Movement.z3
        Movement.z2 = Movement.z3

        while Movement.x < 185:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.x = Movement.x+Movement.step
            Movement.x1 = Movement.x1-Movement.step
            Movement.x2 = Movement.x2+Movement.step*(1/math.sqrt(2))
            Movement.y1 = Movement.y1+Movement.step*(1/math.sqrt(2))
            Movement.z1 = -(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
            time.sleep(Movement.wait)

        while Movement.x > 85:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y, Movement.z1)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y, Movement.z1)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y, Movement.z1)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.x = Movement.x-Movement.step
            Movement.x1 = Movement.x1+Movement.step
            Movement.x2 = Movement.x2-Movement.step*(1/math.sqrt(2))
            Movement.y1 = Movement.y1-Movement.step*(1/math.sqrt(2))
            Movement.z1 = -(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
            time.sleep(Movement.wait)

    def sinistraUscita(self):
        while Movement.x < 135:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z1)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, -Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, -Movement.y1, Movement.z1)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.x = Movement.x+Movement.step
            Movement.x1 = Movement.x1-Movement.step
            Movement.x2 = Movement.x2+Movement.step*(1/math.sqrt(2))
            Movement.y1 = Movement.y1+Movement.step*(1/math.sqrt(2))
            Movement.z1 = -(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
            time.sleep(Movement.wait)

        while Movement.z1 > -130:
            coxaS = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z1)
            coxaD = 180-coxaS
            femurS = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z1)
            femurD = 180-femurS
            tibiaS = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z1)
            tibiaD = 180-tibiaS

            ad2 = coxaD+Movement.off_a_dx_2
            fd2 = femurD+Movement.off_f_dx_2
            td2 = tibiaD+Movement.off_t_dx_2

            as1 = coxaS+Movement.off_a_sx_1
            fs1 = femurS+Movement.off_f_sx_1
            ts1 = tibiaS+Movement.off_t_sx_1

            as3 = coxaS+Movement.off_a_sx_3
            fs3 = femurS+Movement.off_f_sx_3
            ts3 = tibiaS+Movement.off_t_sx_3

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.z1 = Movement.z1-Movement.step
            time.sleep(Movement.wait)

    def ruotaSinistra(self):
        Movement.z2 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z2 < -80:
                coxaS = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z2)
                coxaD = 180-coxaS
                femurS = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z2)
                femurD = 180-femurS
                tibiaS = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z2)
                tibiaD = 180-tibiaS

                ad1 = coxaD+Movement.off_a_dx_1
                fd1 = femurD+Movement.off_f_dx_1
                td1 = tibiaD+Movement.off_t_dx_1

                ad3 = coxaD+Movement.off_a_dx_3
                fd3 = femurD+Movement.off_f_dx_3
                td3 = tibiaD+Movement.off_t_dx_3

                as2 = coxaS+Movement.off_a_sx_2
                fs2 = femurS+Movement.off_f_sx_2
                ts2 = tibiaS+Movement.off_t_sx_2

                Movement.right.servo[2].angle = ad1
                Movement.right.servo[1].angle = fd1
                Movement.right.servo[0].angle = td1

                Movement.right.servo[13].angle = ad3
                Movement.right.servo[14].angle = fd3
                Movement.right.servo[15].angle = td3
                Movement.left.servo[5].angle = as2
                Movement.left.servo[6].angle = fs2
                Movement.left.servo[7].angle = ts2

                Movement.z2 = Movement.z2+Movement.step
                time.sleep(Movement.wait)

        Movement.firstStep = 0
        Movement.z1 = Movement.z2

        while Movement.y < 52:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y+Movement.step
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
            time.sleep(Movement.wait)

        while Movement.y > -52:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y-Movement.step
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
            time.sleep(Movement.wait)

    def ruotaSinistraUscita(self):
        while Movement.y < 0:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y+Movement.step
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
            time.sleep(Movement.wait)

        while Movement.z2 > -130:
            coxaS = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z2)
            coxaD = 180-coxaS
            femurS = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z2)
            femurD = 180-femurS
            tibiaS = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z2)
            tibiaD = 180-tibiaS

            ad1 = coxaD+Movement.off_a_dx_1
            fd1 = femurD+Movement.off_f_dx_1
            td1 = tibiaD+Movement.off_t_dx_1

            ad3 = coxaD+Movement.off_a_dx_3
            fd3 = femurD+Movement.off_f_dx_3
            td3 = tibiaD+Movement.off_t_dx_3

            as2 = coxaS+Movement.off_a_sx_2
            fs2 = femurS+Movement.off_f_sx_2
            ts2 = tibiaS+Movement.off_t_sx_2

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.z2 = Movement.z2-Movement.step
            time.sleep(Movement.wait)

        Movement.firstStep = 1

    def ruotaDestra(self):
        Movement.z2 = Movement.z
        if Movement.firstStep == 1:
            while Movement.z2 < -80:
                coxaS = Movement.braccio1.calcoloIK_joint1(
                    Movement.x, Movement.y, Movement.z2)
                coxaD = 180-coxaS
                femurS = Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z2)
                femurD = 180-femurS
                tibiaS = Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z2)
                tibiaD = 180-tibiaS

                ad1 = coxaD+Movement.off_a_dx_1
                fd1 = femurD+Movement.off_f_dx_1
                td1 = tibiaD+Movement.off_t_dx_1

                ad3 = coxaD+Movement.off_a_dx_3
                fd3 = femurD+Movement.off_f_dx_3
                td3 = tibiaD+Movement.off_t_dx_3

                as2 = coxaS+Movement.off_a_sx_2
                fs2 = femurS+Movement.off_f_sx_2
                ts2 = tibiaS+Movement.off_t_sx_2

                Movement.right.servo[2].angle = ad1
                Movement.right.servo[1].angle = fd1
                Movement.right.servo[0].angle = td1

                Movement.right.servo[13].angle = ad3
                Movement.right.servo[14].angle = fd3
                Movement.right.servo[15].angle = td3
                Movement.left.servo[5].angle = as2
                Movement.left.servo[6].angle = fs2
                Movement.left.servo[7].angle = ts2

                Movement.z2 = Movement.z2+Movement.step
                time.sleep(Movement.wait)

        Movement.firstStep = 0
        Movement.z1 = Movement.z2

        while Movement.y > -52:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y-Movement.step
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
            time.sleep(Movement.wait)

        while Movement.y < 52:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y+Movement.step
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
            time.sleep(Movement.wait)

    def ruotaDestraUscita(self):
        while Movement.y > 0:
            ad1 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_a_dx_1
            fd1 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_f_dx_1
            td1 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)+Movement.off_t_dx_1

            ad2 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z)+Movement.off_a_dx_2
            fd2 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z)+Movement.off_f_dx_2
            td2 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z)+Movement.off_t_dx_2

            ad3 = 180-Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_a_dx_3
            fd3 = 180-Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_f_dx_3
            td3 = 180-Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z2)+Movement.off_t_dx_3

            as1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_a_sx_1
            fs1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_f_sx_1
            ts1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x2, Movement.y1, Movement.z)+Movement.off_t_sx_1

            as2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_a_sx_2
            fs2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_f_sx_2
            ts2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, -Movement.y, Movement.z1)+Movement.off_t_sx_2

            as3 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_a_sx_3
            fs3 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_f_sx_3
            ts3 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z)+Movement.off_t_sx_3

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[5].angle = ad2
            Movement.right.servo[6].angle = fd2
            Movement.right.servo[7].angle = td2

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[13].angle = as1
            Movement.left.servo[14].angle = fs1
            Movement.left.servo[15].angle = ts1

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.left.servo[2].angle = as3
            Movement.left.servo[1].angle = fs3
            Movement.left.servo[0].angle = ts3

            Movement.y = Movement.y-Movement.step
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
            time.sleep(Movement.wait)

        while Movement.z2 > -130:
            coxaS = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z2)
            coxaD = 180-coxaS
            femurS = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z2)
            femurD = 180-femurS
            tibiaS = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z2)
            tibiaD = 180-tibiaS

            ad1 = coxaD+Movement.off_a_dx_1
            fd1 = femurD+Movement.off_f_dx_1
            td1 = tibiaD+Movement.off_t_dx_1

            ad3 = coxaD+Movement.off_a_dx_3
            fd3 = femurD+Movement.off_f_dx_3
            td3 = tibiaD+Movement.off_t_dx_3

            as2 = coxaS+Movement.off_a_sx_2
            fs2 = femurS+Movement.off_f_sx_2
            ts2 = tibiaS+Movement.off_t_sx_2

            Movement.right.servo[2].angle = ad1
            Movement.right.servo[1].angle = fd1
            Movement.right.servo[0].angle = td1

            Movement.right.servo[13].angle = ad3
            Movement.right.servo[14].angle = fd3
            Movement.right.servo[15].angle = td3

            Movement.left.servo[5].angle = as2
            Movement.left.servo[6].angle = fs2
            Movement.left.servo[7].angle = ts2

            Movement.z2 = Movement.z2-Movement.step
            time.sleep(Movement.wait)

        Movement.firstStep = 1


ophelia = Movement()
ophelia.chiusura()

while not rospy.is_shutdown():
    #rospy.init_node('listener', anonymous=True)
    data = rospy.wait_for_message('/chatter', String)
    if data.data == "w":
        if alzato == 1:
            if Movement.dataOld == data.data:
                print("avanti")
                ophelia.avanti()
            elif Movement.dataOld == "x":
                print("indietroUscita")
                ophelia.indietroUscita()
            elif Movement.dataOld == "":
                print("avanti")
                ophelia.avanti()
            elif Movement.dataOld == "s":
                print("avanti")
                ophelia.avanti()
            elif Movement.dataOld == "a":
                print("sinistraUscita")
                ophelia.sinistraUscita()
            elif Movement.dataOld == "d":
                print("destraUscita")
                ophelia.destraUscita()
            elif Movement.dataOld == "q":
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()
            elif Movement.dataOld == "e":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()
            else:
                print("avantiUscita")
                ophelia.avantiUscita()

    elif data.data == "x":
        if alzato == 1:
            if Movement.dataOld == data.data:
                print("indietro")
                ophelia.indietro()
            elif Movement.dataOld == "w":
                print("avantiUscita")
                ophelia.avantiUscita()
            elif Movement.dataOld == "":
                print("indietro")
                ophelia.indietro()
            elif Movement.dataOld == "s":
                print("indietro")
                ophelia.indietro()
            elif Movement.dataOld == "a":
                print("sinistraUscita")
                ophelia.sinistraUscita()
            elif Movement.dataOld == "d":
                print("destraUscita")
                ophelia.destraUscita()
            elif Movement.dataOld == "q":
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()
            elif Movement.dataOld == "e":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()
            else:
                print("indietroUscita")
                ophelia.indietroUscita()

    elif data.data == "e":
        if alzato == 1:
            if Movement.dataOld == data.data:
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()
            elif Movement.dataOld == "w":
                print("avantiUscita")
                ophelia.avantiUscita()
            elif Movement.dataOld == "":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()
            elif Movement.dataOld == "s":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()
            elif Movement.dataOld == "a":
                print("sinistraUscita")
                ophelia.sinistraUscita()
            elif Movement.dataOld == "d":
                print("destraUscita")
                ophelia.destraUscita()
            elif Movement.dataOld == "q":
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()
            elif Movement.dataOld == "x":
                print("indietroUscita")
                ophelia.indietroUscita()
            else:
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()

    elif data.data == "q":
        if alzato == 1:
            if Movement.dataOld == data.data:
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()
            elif Movement.dataOld == "w":
                print("avantiUscita")
                ophelia.avantiUscita()
            elif Movement.dataOld == "":
                print("ruotaSinistraUscita")
                ophelia.ruotaDestraUscita()
            elif Movement.dataOld == "s":
                print("ruotaSinistraUscita")
                ophelia.ruotaDestraUscita()
            elif Movement.dataOld == "a":
                print("sinistraUscita")
                ophelia.sinistraUscita()
            elif Movement.dataOld == "d":
                print("destraUscita")
                ophelia.destraUscita()
            elif Movement.dataOld == "e":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()
            elif Movement.dataOld == "x":
                print("indietroUscita")
                ophelia.indietroUscita()
            else:
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()

    elif data.data == "a":
        if alzato == 1:
            if Movement.dataOld == data.data:
                print("sinistra")
                ophelia.sinistra()
            elif Movement.dataOld == "w":
                print("avantiUscita")
                ophelia.avantiUscita()
            elif Movement.dataOld == "":
                print("sinistra")
                ophelia.sinistra()
            elif Movement.dataOld == "s":
                print("sinistra")
                ophelia.sinistraUscita()
            elif Movement.dataOld == "x":
                print("indietroUscita")
                ophelia.indietroUscita()
            elif Movement.dataOld == "d":
                print("destraUscita")
                ophelia.destraUscita()
            elif Movement.dataOld == "q":
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()
            elif Movement.dataOld == "e":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()
            else:
                print("sinistraUscita")
                ophelia.sinistraUscita()

    elif data.data == "d":
        if alzato == 1:
            if Movement.dataOld == data.data:
                print("destra")
                ophelia.destra()
            elif Movement.dataOld == "w":
                print("avantiUscita")
                ophelia.avantiUscita()
            elif Movement.dataOld == "":
                print("destra")
                ophelia.destra()
            elif Movement.dataOld == "s":
                print("destra")
                ophelia.destra()
            elif Movement.dataOld == "x":
                print("indietroUscita")
                ophelia.indietroUscita()
            elif Movement.dataOld == "d":
                print("destraUscita")
                ophelia.destraUscita()
            elif Movement.dataOld == "q":
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()
            elif Movement.dataOld == "e":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()
            else:
                print("destraUscita")
                ophelia.destraUscita()

    elif data.data == "s":
        if alzato == 1:
            if Movement.dataOld == "w":
                print("avantiUscita")
                ophelia.avantiUscita()
            elif Movement.dataOld == "x":
                print("indietroUscita")
                ophelia.indietroUscita()
            elif Movement.dataOld == "a":
                print("sinistraiUscita")
                ophelia.sinistraUscita()
            elif Movement.dataOld == "d":
                print("destraUscita")
                ophelia.destraUscita()
            elif Movement.dataOld == "q":
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()
            elif Movement.dataOld == "e":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()

    if alzato == 0:
        if data.data == "z":
            if Movement.dataOld == "w":
                print("avantiUscita")
                ophelia.avantiUscita()
            elif Movement.dataOld == "z":
                print("alza")
                ophelia.alza()
                alzato = 1
            elif Movement.dataOld == "x":
                print("indietroUscita")
                ophelia.indietroUscita()
            elif Movement.dataOld == "a":
                print("sinistraiUscita")
                ophelia.sinistraUscita()
            elif Movement.dataOld == "d":
                print("destraUscita")
                ophelia.destraUscita()
            elif Movement.dataOld == "q":
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()
            elif Movement.dataOld == "e":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()

    if alzato == 1:
        if data.data == "c":
            if Movement.dataOld == "w":
                print("avantiUscita")
                ophelia.avantiUscita()
            elif Movement.dataOld == "c":
                print("abbassa")
                ophelia.abbassa()
                alzato = 0
            elif Movement.dataOld == "x":
                print("indietroUscita")
                ophelia.indietroUscita()
            elif Movement.dataOld == "a":
                print("sinistraiUscita")
                ophelia.sinistraUscita()
            elif Movement.dataOld == "d":
                print("destraUscita")
                ophelia.destraUscita()
            elif Movement.dataOld == "q":
                print("ruotaSinistraUscita")
                ophelia.ruotaSinistraUscita()
            elif Movement.dataOld == "e":
                print("ruotaDestraUscita")
                ophelia.ruotaDestraUscita()

    Movement.dataOld = data.data

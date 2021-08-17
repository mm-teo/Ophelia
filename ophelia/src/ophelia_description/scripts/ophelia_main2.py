#! /usr/bin/env python

import time
import rospy
import math
from traiettoria import Cinematica
from sensor_msgs.msg import JointState
from std_msgs.msg import String
from std_msgs.msg import Header
from pynput import keyboard


class Movement:
    def __init__(self):
        pass

    # def posizione base
    x = 135.0
    y = 0.0
    z = -31.0

    pub = rospy.Publisher('/joint_states', JointState, queue_size=1)
    rospy.init_node('joint_state_publisher')
    rate = rospy.Rate(50)
    move = JointState()
    braccio1 = Cinematica()

    x1 = x
    x2 = x
    z1 = z
    z2 = z
    y1 = y
    y2 = y

    dx_a_1 = 0
    dx_f_1 = 0
    dx_t_1 = 0
    dx_a_2 = 0
    dx_f_2 = 0
    dx_t_2 = 0
    dx_a_3 = 0
    dx_f_3 = 0
    dx_t_3 = 0
    sx_a_1 = 0
    sx_f_1 = 0
    sx_t_1 = 0
    sx_a_2 = 0
    sx_f_2 = 0
    sx_t_2 = 0
    sx_a_3 = 0
    sx_f_3 = 0
    sx_t_3 = 0

    firstStep = 1
    dataOld = ""

    def moving(self):
        Movement.move.header = Header()
        Movement.move.name = ['anca_dx_1_joint', 'femore_dx_1_joint', 'tibia_dx_1_joint', 'anca_dx_2_joint', 'femore_dx_2_joint', 'tibia_dx_2_joint', 'anca_dx_3_joint', 'femore_dx_3_joint',
                              'tibia_dx_3_joint', 'anca_sx_1_joint', 'femore_sx_1_joint', 'tibia_sx_1_joint', 'anca_sx_2_joint', 'femore_sx_2_joint', 'tibia_sx_2_joint', 'anca_sx_3_joint', 'femore_sx_3_joint', 'tibia_sx_3_joint']
        Movement.move.position = (Movement.dx_a_1, Movement.dx_f_1, Movement.dx_t_1, Movement.dx_a_2, Movement.dx_f_2, Movement.dx_t_2, Movement.dx_a_3, Movement.dx_f_3,
                                  Movement.dx_t_3, Movement.sx_a_1, Movement.sx_f_1, Movement.sx_t_1, Movement.sx_a_2, Movement.sx_f_2, Movement.sx_t_2, Movement.sx_a_3, Movement.sx_f_3, Movement.sx_t_3)
        Movement.move.velocity = []
        Movement.move.effort = []
        Movement.move.header.stamp = rospy.Time.now()

    def pubb(self):
        Movement.pub.publish(Movement.move)
        # print(Movement.dx_a_1,Movement.dx_f_1,Movement.dx_t_1)
        Movement.rate.sleep()

    def avanti(self):
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

                ophelia.moving()
                Movement.z3 = Movement.z3+1
                ophelia.pubb()

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
                Movement.x, Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z1)

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
                    Movement.x, Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, Movement.y1, Movement.z2)

            ophelia.moving()
            Movement.y = Movement.y-1
            Movement.x1 = Movement.x1-(1/math.sqrt(2))
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.01875+100)
            Movement.z2 = -0.0375*math.pow(Movement.x1-135, 2)-100
            ophelia.pubb()

        while Movement.y < 40:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x1, Movement.y1, Movement.z2)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x1, Movement.y1, Movement.z2)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x1, Movement.y1, Movement.z2)

            Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z)

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
                    Movement.x, Movement.y, Movement.z1)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z1)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z1)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, Movement.y1, Movement.z)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, Movement.y1, Movement.z)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, Movement.y1, Movement.z)

            ophelia.moving()
            Movement.y = Movement.y+1
            Movement.x1 = Movement.x1+(1/math.sqrt(2))
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.01875+100)
            Movement.z2 = -0.0375*math.pow(Movement.x1-135, 2)-100
            ophelia.pubb()

    def avantiUscita(self):
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
                Movement.x, Movement.y, Movement.z1)
            Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z1)
            Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z1)

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
                    Movement.x, Movement.y, Movement.z)
            Movement.sx_f_2 = - \
                Movement.braccio1.calcoloIK_joint2(
                    Movement.x, Movement.y, Movement.z)
            Movement.sx_t_2 = - \
                Movement.braccio1.calcoloIK_joint3(
                    Movement.x, Movement.y, Movement.z)

            Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(
                -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_f_3 = - \
                Movement.braccio1.calcoloIK_joint2(
                    -Movement.x1, Movement.y1, Movement.z2)
            Movement.sx_t_3 = - \
                Movement.braccio1.calcoloIK_joint3(
                    -Movement.x1, Movement.y1, Movement.z2)

            ophelia.moving()
            Movement.y = Movement.y-1
            Movement.x1 = Movement.x1-(1/math.sqrt(2))
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.01875+100)
            Movement.z2 = -0.0375*math.pow(Movement.x1-135, 2)-100
            ophelia.pubb()

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

            ophelia.moving()
            Movement.z2 = Movement.z2-1
            ophelia.pubb()

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

                ophelia.moving()
                Movement.z3 = Movement.z3+1
                ophelia.pubb()

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

            ophelia.moving()
            Movement.y = Movement.y-1
            Movement.x1 = Movement.x1+(1/math.sqrt(2))
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.01875+100)
            Movement.z2 = -0.0375*math.pow(Movement.x1-135, 2)-100
            ophelia.pubb()

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

            ophelia.moving()
            Movement.y = Movement.y+1
            Movement.x1 = Movement.x1-(1/math.sqrt(2))
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.01875+100)
            Movement.z2 = -0.0375*math.pow(Movement.x1-135, 2)-100
            ophelia.pubb()

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

            ophelia.moving()
            Movement.y = Movement.y-1
            Movement.x1 = Movement.x1+(1/math.sqrt(2))
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = -Movement.x1+135
            Movement.z1 = -(Movement.y*Movement.y*0.01875+100)
            Movement.z2 = -0.0375*math.pow(Movement.x1-135, 2)-100
            ophelia.pubb()

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

            ophelia.moving()
            Movement.z2 = Movement.z2-1
            ophelia.pubb()

    def alza(self):
        while Movement.z > -130:
            # destra destri a=anca, f=femore, t=tibia
            Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(
                Movement.x, Movement.y, Movement.z)
            Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(
                Movement.x, Movement.y, Movement.z)
            Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(
                Movement.x, Movement.y, Movement.z)

            Movement.dx_a_2 = Movement.dx_a_1
            Movement.dx_f_2 = Movement.dx_f_1
            Movement.dx_t_2 = Movement.dx_t_1

            Movement.dx_a_3 = Movement.dx_a_1
            Movement.dx_f_3 = Movement.dx_f_1
            Movement.dx_t_3 = Movement.dx_t_1

            Movement.sx_a_1 = Movement.dx_a_1
            Movement.sx_f_1 = -Movement.dx_f_1
            Movement.sx_t_1 = -Movement.dx_t_1

            Movement.sx_a_2 = Movement.dx_a_1
            Movement.sx_f_2 = -Movement.dx_f_1
            Movement.sx_t_2 = -Movement.dx_t_1

            Movement.sx_a_3 = Movement.dx_a_1
            Movement.sx_f_3 = -Movement.dx_f_1
            Movement.sx_t_3 = -Movement.dx_t_1

            ophelia.moving()
            Movement.z = Movement.z-1
            ophelia.pubb()

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

                ophelia.moving()
                Movement.z3 = Movement.z3+1
                ophelia.pubb()

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

            ophelia.moving()
            Movement.x = Movement.x-1
            Movement.x1 = Movement.x1+1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = Movement.y1-(1/math.sqrt(2))
            ophelia.pubb()

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

            ophelia.moving()
            Movement.x = Movement.x+1
            Movement.x1 = Movement.x1-1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = Movement.y1+(1/math.sqrt(2))
            ophelia.pubb()

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

            ophelia.moving()
            Movement.x = Movement.x-1
            Movement.x1 = Movement.x1+1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = Movement.y1-(1/math.sqrt(2))
            ophelia.pubb()

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

            ophelia.moving()
            Movement.z2 = Movement.z2-1
            ophelia.pubb()

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

                ophelia.moving()
                Movement.z3 = Movement.z3+1
                ophelia.pubb()

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

            ophelia.moving()
            Movement.x = Movement.x+1
            Movement.x1 = Movement.x1-1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = Movement.y1+(1/math.sqrt(2))
            ophelia.pubb()

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

            ophelia.moving()
            Movement.x = Movement.x-1
            Movement.x1 = Movement.x1+1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2-(1/math.sqrt(2))
            Movement.y1 = Movement.y1-(1/math.sqrt(2))
            ophelia.pubb()

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

            ophelia.moving()
            Movement.x = Movement.x+1
            Movement.x1 = Movement.x1-1
            Movement.z1 = -(Movement.x*Movement.x *
                            0.01875+441.7-5.065*Movement.x)
            Movement.x2 = Movement.x2+(1/math.sqrt(2))
            Movement.y1 = Movement.y1+(1/math.sqrt(2))
            ophelia.pubb()

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

            ophelia.moving()
            Movement.z2 = Movement.z2-1
            ophelia.pubb()

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

                ophelia.moving()
                Movement.z3 = Movement.z3+1
                ophelia.pubb()

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

            ophelia.moving()
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
            ophelia.pubb()

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

            ophelia.moving()
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
            ophelia.pubb()

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

            ophelia.moving()
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
            ophelia.pubb()
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

            ophelia.moving()
            Movement.z2 = Movement.z2-1
            ophelia.pubb()

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

                ophelia.moving()
                Movement.z3 = Movement.z3+1
                ophelia.pubb()

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

            ophelia.moving()
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
            ophelia.pubb()

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

            ophelia.moving()
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
            ophelia.pubb()

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

            ophelia.moving()
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
            ophelia.pubb()
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

            ophelia.moving()
            Movement.z2 = Movement.z2-1
            ophelia.pubb()

        Movement.firstStep = 0


ophelia = Movement()
ophelia.alza()
w = 0

while not rospy.is_shutdown():
    data = rospy.wait_for_message('/chatter', String)
    print(data)
    print("OLD  == " + Movement.dataOld)
    if data.data == "w":
        print("aaaa")
        if Movement.dataOld == data.data or Movement.dataOld == "":
            print("avanti")
            ophelia.avanti()
            Movement.dataOld = "w"
        elif Movement.dataOld == "s":
            print("indietro_uscita")
            ophelia.indietroUscita()
            Movement.dataOld = ""
        elif Movement.dataOld == "a":
            print("sinistra_uscita")
            ophelia.ruotaSinistraUscita()
            Movement.dataOld = ""
        elif Movement.dataOld == "d":
            print("destra_uscita")
            ophelia.ruotaDestraUscita()
            Movement.dataOld = ""
        else:
          print("BBBB")
    elif data.data == "s":
        if Movement.dataOld == data.data or Movement.dataOld == "":
            print("indietro")
            ophelia.indietro()
            Movement.dataOld = "s"
        elif Movement.dataOld == "w":
            print("avanti_uscita")
            ophelia.avantiUscita()
            Movement.dataOld = ""
        elif Movement.dataOld == "a":
            print("sinistra_uscita")
            ophelia.ruotaSinistraUscita()
            Movement.dataOld = ""
        elif Movement.dataOld == "d":
            print("destra_uscita")
            ophelia.ruotaDestraUscita()
            Movement.dataOld = ""
    elif data.data == "a":
        if Movement.dataOld == data.data or Movement.dataOld == "":
            print("routa_sinistra")
            ophelia.ruotaSinistra()
            Movement.dataOld = "a"
        elif Movement.dataOld == "w":
            print("avanti_uscita")
            ophelia.avantiUscita()
            Movement.dataOld = ""
        elif Movement.dataOld == "s":
            print("indietro_uscita")
            ophelia.indietroUscita()
            Movement.dataOld = ""
        elif Movement.dataOld == "d":
            print("destra_uscita")
            ophelia.ruotaDestraUscita()
            Movement.dataOld = ""
    elif data.data == "d":
        if Movement.dataOld == data.data or Movement.dataOld == "":
            print("routa_destra")
            ophelia.ruotaDestra()
            Movement.dataOld = "d"
        elif Movement.dataOld == "w":
            print("avanti_uscita")
            ophelia.avantiUscita()
            Movement.dataOld = ""
        elif Movement.dataOld == "s":
            print("indietro_uscita")
            ophelia.indietroUscita()
            Movement.dataOld = ""
        elif Movement.dataOld == "a":
            print("sinistra_uscita")
            ophelia.ruotaSinistraUscita()
            Movement.dataOld = ""
    elif data.data == "z":
        if Movement.dataOld == data.data or Movement.dataOld == "":
            print("stop")
        elif Movement.dataOld == "a":
            print("sinistra_uscita")
            ophelia.ruotaSinistraUscita()
        elif Movement.dataOld == "d":
            print("destra_uscita")
            ophelia.ruotaDestraUscita()
        elif Movement.dataOld == "w":
            print("avanti_uscita")
            ophelia.avantiUscita()
        elif Movement.dataOld == "d":
            print("indietro_uscita")
            ophelia.indietroUscita()
        Movement.dataOld = ""

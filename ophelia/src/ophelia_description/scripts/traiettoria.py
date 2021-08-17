#! /usr/bin/env python

import rospy
import math

a = 49.8  # lungheza anca
f = 76.2  # lunghezza femore
t = 136.4  # lunghezza tibia

x = 135.0
y = 0.0
z = -31.0

# start 135 0 -31


class Cinematica:
    def __init__(self):
        pass

    def calcoloIK_joint1(self, x, y, z):
        self.x = x  # pos X
        self.y = y  # pos Y
        self.z = z  # pos Z
        # calcolo angolo c=gamma
        c = math.atan(y/x)
        th1_r = c  # theta1 in radianti anca
        return(th1_r)

    def calcoloIK_joint2(self, x, y, z):
        self.x = x  # pos X
        self.y = y  # pos Y
        self.z = z  # pos Z
        # calcoli angoli a1=alfa1 e a2=alfa2
        l1 = (math.sqrt(math.pow(x, 2)+math.pow(y, 2)))-a
        l2 = math.sqrt(math.pow(l1, 2)+math.pow(z, 2))
        a1 = math.asin((l1)/(l2))
        a2 = math.acos(
            (math.pow(f, 2)-math.pow(t, 2)+math.pow(l2, 2))/(2*f*l2))
        th2_r = (a1+a2)-(math.pi/2)  # theta2 in radianti femore
        return(th2_r)

    def calcoloIK_joint3(self, x, y, z):
        self.x = x  # pos X
        self.y = y  # pos Y
        self.z = z  # pos Z
        # calcolo angolo b=beta
        b = math.acos((math.pow(t, 2)+math.pow(f, 2)-math.pow(x, 2)-math.pow(y, 2)-math.pow(
            a, 2)-math.pow(z, 2)+(2*a*math.sqrt(math.pow(x, 2)+math.pow(y, 2))))/(2*f*t))
        th3_r = -((math.pi/2)-b)  # theta2 in radianti femore
        return(th3_r)

# puntoUno=Cinematica()
# a1=puntoUno.calcoloIK_joint1(135, 0, -31)
# a2=puntoUno.calcoloIK_joint2(135, 0, -31)
# a3=puntoUno.calcoloIK_joint3(135, 0, -31)
# print(a1,a2,a3)

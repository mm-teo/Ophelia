#! /usr/bin/env python

from math import pow, sqrt, atan, asin, acos, pi


class Cinematica:
    __slots__ = 'a', 'f', 't'

    def __init__(self, anca=49.8, femore=76.2, tibia=136.4):
        self.a = anca
        self.f = femore
        self.t = tibia

    def calcoloIK_joint1(self, x, y, z):
        # calcolo angolo c=gamma
        c = atan(y/x)
        th1_r = c  # theta1 in radianti anca
        return(th1_r)

    def calcoloIK_joint2(self, x, y, z):
        # calcoli angoli a1=alfa1 e a2=alfa2
        l1 = (sqrt(pow(x, 2)+pow(y, 2)))-self.a
        l2 = sqrt(pow(l1, 2)+pow(z, 2))
        a1 = asin((l1)/(l2))
        a2 = acos((pow(self.f, 2)-pow(self.t, 2)+pow(l2, 2)) / (2*self.f*l2))
        th2_r = (a1+a2)-(pi/2)  # theta2 in radianti femore
        return(th2_r)

    def calcoloIK_joint3(self, x, y, z):
        # calcolo angolo b=beta
        temp = pow(self.t, 2)+pow(self.f, 2)-pow(x, 2)-pow(y, 2) \
            - pow(self.a, 2)-pow(z, 2)+(2*self.a*sqrt(pow(x, 2)+pow(y, 2)))
        b = acos(temp/(2*self.f*self.t))
        th3_r = -((pi/2)-b)  # theta2 in radianti femore
        return th3_r

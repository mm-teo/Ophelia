#! /usr/bin/env python

import time
import math
from traiettoria import Cinematica
from adafruit_servokit import ServoKit
from adafruit_servokit_2 import ServoKit2


class Movement:
  def __init__(self):
    pass

  #def posizione base
  x=135.0
  y=0.0
  z=-31.0

  wait=0
  braccio1 = Cinematica()
  right = ServoKit(channels=16)
  left = ServoKit2(channels=16)

  off_a_dx_1=6
  off_a_dx_2=16
  off_a_dx_3=-5
  off_f_dx_1=13
  off_f_dx_2=23
  off_f_dx_3=21
  off_t_dx_1=-10
  off_t_dx_2=-10
  off_t_dx_3=-10

  off_a_sx_1=0
  off_a_sx_2=7
  off_a_sx_3=16
  off_f_sx_1=-10
  off_f_sx_2=-20
  off_f_sx_3=-15
  off_t_sx_1=10
  off_t_sx_2=10
  off_t_sx_3=10

  x1=x
  x2=x
  z1=z
  z2=z
  y1=y
  y2=y

  firstStep = 1
  dataOld=""

  def chiusura(self):
    coxaS=Movement.braccio1.calcoloIK_joint1(135,0,-31)
    coxaD=180-coxaS
    femurS=Movement.braccio1.calcoloIK_joint2(135,0,-31)
    femurD=180-femurS
    tibiaS=Movement.braccio1.calcoloIK_joint3(135,0,-31)
    tibiaD=180-tibiaS

    Movement.right.servo[2].angle = coxaD+Movement.off_a_dx_1
    Movement.right.servo[1].angle = femurD+Movement.off_f_dx_1
    Movement.right.servo[0].angle = tibiaD+Movement.off_t_dx_1

    Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
    Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
    Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

    Movement.right.servo[13].angle = coxaD+Movement.off_a_dx_3
    Movement.right.servo[14].angle = femurD+Movement.off_f_dx_3
    Movement.right.servo[15].angle = tibiaD+Movement.off_t_dx_3

    Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
    Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
    Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

    Movement.left.servo[5].angle = coxaS+Movement.off_a_sx_2
    Movement.left.servo[6].angle = femurS+Movement.off_f_sx_2
    Movement.left.servo[7].angle = tibiaS+Movement.off_t_sx_2

    Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
    Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
    Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3

  def alza(self):
    while Movement.z>-130:
      coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z)
      coxaD=180-coxaS
      femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z)
      femurD=180-femurS
      tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z)
      tibiaD=180-tibiaS

      Movement.right.servo[2].angle = coxaD+Movement.off_a_dx_1
      Movement.right.servo[1].angle = femurD+Movement.off_f_dx_1
      Movement.right.servo[0].angle = tibiaD+Movement.off_t_dx_1

      Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
      Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
      Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

      Movement.right.servo[13].angle = coxaD+Movement.off_a_dx_3
      Movement.right.servo[14].angle = femurD+Movement.off_f_dx_3
      Movement.right.servo[15].angle = tibiaD+Movement.off_t_dx_3

      Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
      Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
      Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

      Movement.left.servo[5].angle = coxaS+Movement.off_a_sx_2
      Movement.left.servo[6].angle = femurS+Movement.off_f_sx_2
      Movement.left.servo[7].angle = tibiaS+Movement.off_t_sx_2

      Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
      Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
      Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3
      Movement.z=Movement.z-1


  def avanti(self):
    Movement.z3=Movement.z
    if Movement.firstStep == 1:
      while Movement.z3<-80:
        coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z3)
        coxaD=180-coxaS
        femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z3)
        femurD=180-femurS
        tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z3)
        tibiaD=180-tibiaS

        Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
        Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
        Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

        Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
        Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
        Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

        Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
        Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
        Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3

        Movement.z3=Movement.z3+1

    Movement.firstStep=0
    Movement.z1=Movement.z3
    Movement.z2=Movement.z3

    while Movement.y>-50:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y1,Movement.z)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y1,Movement.z)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y1,Movement.z)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z1)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z1)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z1)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x,-Movement.y,Movement.z)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x,-Movement.y,Movement.z)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x,-Movement.y,Movement.z)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_t_sx_3

      Movement.y=Movement.y-1
      Movement.x1=Movement.x1-(1/math.sqrt(2))
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)


    while Movement.y<50:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y1,Movement.z2)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y1,Movement.z2)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y1,Movement.z2)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z2)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z2)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z2)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x,-Movement.y,Movement.z1)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x,-Movement.y,Movement.z1)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x,-Movement.y,Movement.z1)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y1,Movement.z)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y1,Movement.z)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y1,Movement.z)+Movement.off_t_sx_3

      Movement.y=Movement.y+1
      Movement.x1=Movement.x1+(1/math.sqrt(2))
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)

  def avantiUscita(self):
    Movement.firstStep=1
    while Movement.y>0:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y1,Movement.z)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y1,Movement.z)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y1,Movement.z)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z1)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z1)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z1)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x,-Movement.y,Movement.z)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x,-Movement.y,Movement.z)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x,-Movement.y,Movement.z)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_t_sx_3

      Movement.y=Movement.y-1
      Movement.x1=Movement.x1-(1/math.sqrt(2))
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)


    while Movement.z2>-130:
      coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z2)
      coxaD=180-coxaS
      femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z2)
      femurD=180-femurS
      tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z2)
      tibiaD=180-tibiaS

      Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
      Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
      Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

      Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
      Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
      Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

      Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
      Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
      Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3

      Movement.z2=Movement.z2-1
      
  def indietro(self):
    Movement.z3=Movement.z
    if Movement.firstStep == 1:
      while Movement.z3<-80:
        coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z3)
        coxaD=180-coxaS
        femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z3)
        femurD=180-femurS
        tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z3)
        tibiaD=180-tibiaS

        Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
        Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
        Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

        Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
        Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
        Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

        Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
        Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
        Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3

        Movement.z3=Movement.z3+1
        
    Movement.firstStep=0
    Movement.z1=Movement.z3
    Movement.z2=Movement.z3

    while Movement.y>-50:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y1,Movement.z)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y1,Movement.z)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y1,Movement.z)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x,-Movement.y,Movement.z1)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x,-Movement.y,Movement.z1)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x,-Movement.y,Movement.z1)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_t_sx_3

      Movement.y=Movement.y-1
      Movement.x1=Movement.x1+(1/math.sqrt(2))
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)
      
    while Movement.y<50:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y1,Movement.z2)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y1,Movement.z2)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y1,Movement.z2)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x,-Movement.y,Movement.z)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x,-Movement.y,Movement.z)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x,-Movement.y,Movement.z)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z2)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z2)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z2)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z1)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z1)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z1)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y1,Movement.z)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y1,Movement.z)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y1,Movement.z)+Movement.off_t_sx_3

      Movement.y=Movement.y+1
      Movement.x1=Movement.x1-(1/math.sqrt(2))
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)
      
  def indietroUscita(self):
    Movement.firstStep=1
    while Movement.y>0:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y1,Movement.z)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y1,Movement.z)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y1,Movement.z)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x,-Movement.y,Movement.z1)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x,-Movement.y,Movement.z1)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x,-Movement.y,Movement.z1)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_t_sx_3

      Movement.y=Movement.y-1
      Movement.x1=Movement.x1+(1/math.sqrt(2))
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)
      
    while Movement.z2>-130:
      coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z2)
      coxaD=180-coxaS
      femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z2)
      femurD=180-femurS
      tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z2)
      tibiaD=180-tibiaS

      Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
      Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
      Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

      Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
      Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
      Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

      Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
      Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
      Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3

      Movement.z2=Movement.z2-1
      
  def destra(self):
    Movement.z3=Movement.z
    if Movement.firstStep == 1:
      while Movement.z3<-80:
        coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z3)
        coxaD=180-coxaS
        femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z3)
        femurD=180-femurS
        tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z3)
        tibiaD=180-tibiaS

        Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
        Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
        Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

        Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
        Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
        Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

        Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
        Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
        Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3

        Movement.z3=Movement.z3+1
        
    Movement.firstStep=0
    Movement.z1=Movement.z3
    Movement.z2=Movement.z3

    print("dx")
    while Movement.x>85:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y,Movement.z1)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y,Movement.z1)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y,Movement.z1)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z1)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z1)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z1)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y,Movement.z)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y,Movement.z)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y,Movement.z)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_t_sx_3

      Movement.x=Movement.x-1
      Movement.x1=Movement.x1+1
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=Movement.y1-(1/math.sqrt(2))
      Movement.z1=-(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
      
    while Movement.x<185:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z1)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z1)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z1)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y,Movement.z)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y,Movement.z)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y,Movement.z)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y,Movement.z1)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y,Movement.z1)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y,Movement.z1)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_sx_3

      Movement.x=Movement.x+1
      Movement.x1=Movement.x1-1
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=Movement.y1+(1/math.sqrt(2))
      Movement.z1=-(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
      
  def destraUscita(self):
    while Movement.x>135:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y,Movement.z1)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y,Movement.z1)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y,Movement.z1)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z1)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z1)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z1)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y,Movement.z)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y,Movement.z)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y,Movement.z)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_t_sx_3

      Movement.x=Movement.x-1
      Movement.x1=Movement.x1+1
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=Movement.y1-(1/math.sqrt(2))
      Movement.z1=-(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
      
    Movement.firstStep=1
    print(Movement.z1)
    while Movement.z1>-130:
      coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z1)
      coxaD=180-coxaS
      femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z1)
      femurD=180-femurS
      tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z1)
      tibiaD=180-tibiaS

      Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
      Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
      Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

      Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
      Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
      Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

      Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
      Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
      Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3

      Movement.z1=Movement.z1-1
      
  def sinistra(self):
    Movement.z3=Movement.z
    if Movement.firstStep == 1:
      while Movement.z3<-80:
        coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z3)
        coxaD=180-coxaS
        femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z3)
        femurD=180-femurS
        tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z3)
        tibiaD=180-tibiaS

        Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
        Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
        Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

        Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
        Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
        Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

        Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
        Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
        Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3

        Movement.z3=Movement.z3+1
        
    Movement.firstStep=0
    Movement.z1=Movement.z3
    Movement.z2=Movement.z3

    print("sx")
    while Movement.x<185:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y,Movement.z1)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y,Movement.z1)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y,Movement.z1)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z1)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z1)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z1)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y,Movement.z)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y,Movement.z)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y,Movement.z)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_t_sx_3

      Movement.x=Movement.x+1
      Movement.x1=Movement.x1-1
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=Movement.y1+(1/math.sqrt(2))
      Movement.z1=-(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
      
    while Movement.x>85:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z1)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z1)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z1)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y,Movement.z)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y,Movement.z)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y,Movement.z)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y,Movement.z1)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y,Movement.z1)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y,Movement.z1)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_sx_3

      Movement.x=Movement.x-1
      Movement.x1=Movement.x1+1
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=Movement.y1-(1/math.sqrt(2))
      Movement.z1=-(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
      
  def sinistraUscita(self):
    while Movement.x<135:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y,Movement.z1)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y,Movement.z1)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y,Movement.z1)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z1)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z1)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z1)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y,Movement.z)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y,Movement.z)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y,Movement.z)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z1)+Movement.off_t_sx_3

      Movement.x=Movement.x+1
      Movement.x1=Movement.x1-1
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=Movement.y1+(1/math.sqrt(2))
      Movement.z1=-(Movement.x*Movement.x*0.02+444.5-5.4*Movement.x)
      
    while Movement.z1>-130:
      coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z1)
      coxaD=180-coxaS
      femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z1)
      femurD=180-femurS
      tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z1)
      tibiaD=180-tibiaS

      Movement.right.servo[5].angle = coxaD+Movement.off_a_dx_2
      Movement.right.servo[6].angle = femurD+Movement.off_f_dx_2
      Movement.right.servo[7].angle = tibiaD+Movement.off_t_dx_2

      Movement.left.servo[13].angle = coxaS+Movement.off_a_sx_1
      Movement.left.servo[14].angle = femurS+Movement.off_f_sx_1
      Movement.left.servo[15].angle = tibiaS+Movement.off_t_sx_1

      Movement.left.servo[2].angle = coxaS+Movement.off_a_sx_3
      Movement.left.servo[1].angle = femurS+Movement.off_f_sx_3
      Movement.left.servo[0].angle = tibiaS+Movement.off_t_sx_3

      Movement.z1=Movement.z1-1
      
  def ruotaDestra(self):
    Movement.z2=Movement.z
    if Movement.firstStep == 1:
      while Movement.z2<-80:
        coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z2)
        coxaD=180-coxaS
        femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z2)
        femurD=180-femurS
        tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z2)
        tibiaD=180-tibiaS

        Movement.right.servo[2].angle = coxaD+Movement.off_a_dx_2
        Movement.right.servo[1].angle = femurD+Movement.off_f_dx_2
        Movement.right.servo[0].angle = tibiaD+Movement.off_t_dx_2

        Movement.right.servo[13].angle = coxaS+Movement.off_a_sx_1
        Movement.right.servo[14].angle = femurS+Movement.off_f_sx_1
        Movement.right.servo[15].angle = tibiaS+Movement.off_t_sx_1

        Movement.left.servo[5].angle = coxaS+Movement.off_a_sx_3
        Movement.left.servo[6].angle = femurS+Movement.off_f_sx_3
        Movement.left.servo[7].angle = tibiaS+Movement.off_t_sx_3

        Movement.z2=Movement.z2+1
        print("["+str(Movement.right.servo[2].angle)+","+str(Movement.right.servo[1].angle)+","+str(Movement.right.servo[0].angle)+","+str(Movement.right.servo[5].angle)+","+str(Movement.right.servo[6].angle)+","+str(Movement.right.servo[7].angle)+","+str(Movement.right.servo[13].angle)+","+str(Movement.right.servo[14].angle)+","+str(Movement.right.servo[15].angle)+","+str(Movement.left.servo[13].angle)+","+str(Movement.left.servo[14].angle)+","+str(Movement.left.servo[15].angle)+","+str(Movement.left.servo[5].angle)+","+str(Movement.left.servo[6].angle)+","+str(Movement.left.servo[7].angle)+","+str(Movement.left.servo[2].angle)+","+str(Movement.left.servo[1].angle)+","+str(Movement.left.servo[0].angle)+"]"+",")


    Movement.firstStep=0
    Movement.z1=Movement.z2
    print("dest")
    while Movement.y<52:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y1,Movement.z2)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y1,Movement.z2)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y1,Movement.z2)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x,-Movement.y,Movement.z)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x,-Movement.y,Movement.z)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x,-Movement.y,Movement.z)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z2)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z2)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z2)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z1)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z1)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z1)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y1,Movement.z)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y1,Movement.z)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y1,Movement.z)+Movement.off_t_sx_3

      Movement.y=Movement.y+1
      Movement.y1=Movement.y*1.199
      b1=134.2
      c1=-36342+math.pow(Movement.y,2)
      Movement.x=(-b1+math.sqrt(math.pow(b1,2)-(4*c1)))/(2)
      Movement.z1=-0.01849*math.pow(Movement.y,2)-80
      Movement.z2=-0.01286*math.pow(Movement.y1,2)-80
      b2=211.2
      c2=-46656+math.pow(Movement.y1,2)+33.6*Movement.y1
      Movement.x1=(-b2+math.sqrt(math.pow(b2,2)-(4*c2)))/(2)

      c3=-46656+math.pow(Movement.y1,2)-33.6*Movement.y1
      Movement.x2=(-b2+math.sqrt(math.pow(b2,2)-(4*c3)))/(2)
      print("["+str(Movement.right.servo[2].angle)+","+str(Movement.right.servo[1].angle)+","+str(Movement.right.servo[0].angle)+","+str(Movement.right.servo[5].angle)+","+str(Movement.right.servo[6].angle)+","+str(Movement.right.servo[7].angle)+","+str(Movement.right.servo[13].angle)+","+str(Movement.right.servo[14].angle)+","+str(Movement.right.servo[15].angle)+","+str(Movement.left.servo[13].angle)+","+str(Movement.left.servo[14].angle)+","+str(Movement.left.servo[15].angle)+","+str(Movement.left.servo[5].angle)+","+str(Movement.left.servo[6].angle)+","+str(Movement.left.servo[7].angle)+","+str(Movement.left.servo[2].angle)+","+str(Movement.left.servo[1].angle)+","+str(Movement.left.servo[0].angle)+"]"+",")



    while Movement.y<50:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y1,Movement.z)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y1,Movement.z)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y1,Movement.z)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x,-Movement.y,Movement.z1)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x,-Movement.y,Movement.z1)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x,-Movement.y,Movement.z1)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z2)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y1,Movement.z2)+Movement.off_t_sx_3

      Movement.y=Movement.y-1
      Movement.y1=Movement.y1-1.199
      b1=134.2
      c1=-36342+math.pow(Movement.y,2)
      Movement.x=(-b1+math.sqrt(math.pow(b1,2)-(4*c1)))/(2)
      Movement.z1=-0.01849*math.pow(Movement.y,2)-80
      Movement.z2=-0.01286*math.pow(Movement.y1,2)-80
      b2=211.2
      c2=-46656+math.pow(Movement.y1,2)+33.6*Movement.y1
      Movement.x1=(-b2+math.sqrt(math.pow(b2,2)-(4*c2)))/(2)
      c3=-46656+math.pow(Movement.y1,2)-33.6*Movement.y1
      Movement.x2=(-b2+math.sqrt(math.pow(b2,2)-(4*c3)))/(2)
      print("["+str(Movement.right.servo[2].angle)+","+str(Movement.right.servo[1].angle)+","+str(Movement.right.servo[0].angle)+","+str(Movement.right.servo[5].angle)+","+str(Movement.right.servo[6].angle)+","+str(Movement.right.servo[7].angle)+","+str(Movement.right.servo[13].angle)+","+str(Movement.right.servo[14].angle)+","+str(Movement.right.servo[15].angle)+","+str(Movement.left.servo[13].angle)+","+str(Movement.left.servo[14].angle)+","+str(Movement.left.servo[15].angle)+","+str(Movement.left.servo[5].angle)+","+str(Movement.left.servo[6].angle)+","+str(Movement.left.servo[7].angle)+","+str(Movement.left.servo[2].angle)+","+str(Movement.left.servo[1].angle)+","+str(Movement.left.servo[0].angle)+"]"+",")


  def ruotaDestraUscita(self):
    while Movement.y<0:
      Movement.right.servo[2].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x1,Movement.y1,Movement.z2)+Movement.off_a_dx_1
      Movement.right.servo[1].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x1,Movement.y1,Movement.z2)+Movement.off_f_dx_1
      Movement.right.servo[0].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x1,Movement.y1,Movement.z2)+Movement.off_t_dx_1

      Movement.right.servo[5].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x,-Movement.y,Movement.z)+Movement.off_a_dx_2
      Movement.right.servo[6].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x,-Movement.y,Movement.z)+Movement.off_f_dx_2
      Movement.right.servo[7].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x,-Movement.y,Movement.z)+Movement.off_t_dx_2

      Movement.right.servo[13].angle = 180-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1,Movement.z2)+Movement.off_a_dx_3
      Movement.right.servo[14].angle = 180-Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1,Movement.z2)+Movement.off_f_dx_3
      Movement.right.servo[15].angle = 180-Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1,Movement.z2)+Movement.off_t_dx_3

      Movement.left.servo[13].angle = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1,Movement.z)+Movement.off_a_sx_1
      Movement.left.servo[14].angle = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1,Movement.z)+Movement.off_f_sx_1
      Movement.left.servo[15].angle = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1,Movement.z)+Movement.off_t_sx_1

      Movement.left.servo[5].angle = Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z1)+Movement.off_a_sx_2
      Movement.left.servo[6].angle = Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z1)+Movement.off_f_sx_2
      Movement.left.servo[7].angle = Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z1)+Movement.off_t_sx_2

      Movement.left.servo[2].angle = Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y1,Movement.z)+Movement.off_a_sx_3
      Movement.left.servo[1].angle = Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y1,Movement.z)+Movement.off_f_sx_3
      Movement.left.servo[0].angle = Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y1,Movement.z)+Movement.off_t_sx_3

      Movement.y=Movement.y+1
      Movement.y1=Movement.y*1.199
      b1=134.2
      c1=-36342+math.pow(Movement.y,2)
      Movement.x=(-b1+math.sqrt(math.pow(b1,2)-(4*c1)))/(2)
      Movement.z1=-0.01849*math.pow(Movement.y,2)-80
      Movement.z2=-0.01286*math.pow(Movement.y1,2)-80
      b2=211.2
      c2=-46656+math.pow(Movement.y1,2)+33.6*Movement.y1
      Movement.x1=(-b2+math.sqrt(math.pow(b2,2)-(4*c2)))/(2)

      c3=-46656+math.pow(Movement.y1,2)-33.6*Movement.y1
      Movement.x2=(-b2+math.sqrt(math.pow(b2,2)-(4*c3)))/(2)
      print("["+str(Movement.right.servo[2].angle)+","+str(Movement.right.servo[1].angle)+","+str(Movement.right.servo[0].angle)+","+str(Movement.right.servo[5].angle)+","+str(Movement.right.servo[6].angle)+","+str(Movement.right.servo[7].angle)+","+str(Movement.right.servo[13].angle)+","+str(Movement.right.servo[14].angle)+","+str(Movement.right.servo[15].angle)+","+str(Movement.left.servo[13].angle)+","+str(Movement.left.servo[14].angle)+","+str(Movement.left.servo[15].angle)+","+str(Movement.left.servo[5].angle)+","+str(Movement.left.servo[6].angle)+","+str(Movement.left.servo[7].angle)+","+str(Movement.left.servo[2].angle)+","+str(Movement.left.servo[1].angle)+","+str(Movement.left.servo[0].angle)+"]"+",")


    while Movement.z2>-130:
      coxaS=Movement.braccio1.calcoloIK_joint1(Movement.x,Movement.y,Movement.z2)
      coxaD=180-coxaS
      femurS=Movement.braccio1.calcoloIK_joint2(Movement.x,Movement.y,Movement.z2)
      femurD=180-femurS
      tibiaS=Movement.braccio1.calcoloIK_joint3(Movement.x,Movement.y,Movement.z2)
      tibiaD=180-tibiaS

      Movement.right.servo[2].angle = coxaD+Movement.off_a_dx_2
      Movement.right.servo[1].angle = femurD+Movement.off_f_dx_2
      Movement.right.servo[0].angle = tibiaD+Movement.off_t_dx_2

      Movement.right.servo[13].angle = coxaS+Movement.off_a_sx_1
      Movement.right.servo[14].angle = femurS+Movement.off_f_sx_1
      Movement.right.servo[15].angle = tibiaS+Movement.off_t_sx_1

      Movement.left.servo[5].angle = coxaS+Movement.off_a_sx_3
      Movement.left.servo[6].angle = femurS+Movement.off_f_sx_3
      Movement.left.servo[7].angle = tibiaS+Movement.off_t_sx_3

      Movement.z2=Movement.z2-1
      print("["+str(Movement.right.servo[2].angle)+","+str(Movement.right.servo[1].angle)+","+str(Movement.right.servo[0].angle)+","+str(Movement.right.servo[5].angle)+","+str(Movement.right.servo[6].angle)+","+str(Movement.right.servo[7].angle)+","+str(Movement.right.servo[13].angle)+","+str(Movement.right.servo[14].angle)+","+str(Movement.right.servo[15].angle)+","+str(Movement.left.servo[13].angle)+","+str(Movement.left.servo[14].angle)+","+str(Movement.left.servo[15].angle)+","+str(Movement.left.servo[5].angle)+","+str(Movement.left.servo[6].angle)+","+str(Movement.left.servo[7].angle)+","+str(Movement.left.servo[2].angle)+","+str(Movement.left.servo[1].angle)+","+str(Movement.left.servo[0].angle)+"]"+",")

    Movement.firstStep=1

ophelia=Movement()
ophelia.alza()
print("destra")
ophelia.ruotaDestra()
print("uscitaDx")
ophelia.ruotaDestraUscita()

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

  #def posizione base
  x=135.0
  y=0.0
  z=-31.0

  pub = rospy.Publisher('/joint_states', JointState, queue_size=1)
  rospy.init_node('joint_state_publisher')
  rate = rospy.Rate(50)
  move = JointState()
  braccio1 = Cinematica()

  x1=x
  x2=x
  z1=z
  z2=z
  y1=y
  y2=y

  dx_a_1=0 
  dx_f_1=0
  dx_t_1=0
  dx_a_2=0
  dx_f_2=0
  dx_t_2=0
  dx_a_3=0
  dx_f_3=0
  dx_t_3=0
  sx_a_1=0
  sx_f_1=0
  sx_t_1=0
  sx_a_2=0
  sx_f_2=0
  sx_t_2=0
  sx_a_3=0
  sx_f_3=0
  sx_t_3=0

  firstStep = 1
  dataOld=""
  
  def moving(self):
    Movement.move.header = Header()
    Movement.move.name = ['anca_dx12_joint', 'femore_dx12_joint', 'tibia_dx12_joint', 'anca_dx21_joint', 'femore_dx21_joint', 'tibia_dx21_joint', 'anca_dx_3_joint', 'femore_dx_3_joint', 'tibia_dx_3_joint', 'anca_sx12_joint', 'femore_sx12_joint', 'tibia_sx12_joint', 'anca_sx21_joint', 'femore_sx21_joint', 'tibia_sx21_joint', 'anca_sx_3_joint', 'femore_sx_3_joint','tibia_sx_3_joint']
    Movement.move.position = (Movement.dx_a_1, Movement.dx_f_1, Movement.dx_t_1, Movement.dx_a_2, Movement.dx_f_2, Movement.dx_t_2, Movement.dx_a_3, Movement.dx_f_3, Movement.dx_t_3, Movement.sx_a_1, Movement.sx_f_1, Movement.sx_t_1, Movement.sx_a_2, Movement.sx_f_2, Movement.sx_t_2, Movement.sx_a_3, Movement.sx_f_3, Movement.sx_t_3)
    Movement.move.velocity = []
    Movement.move.effort = []
    Movement.move.header.stamp = rospy.Time.now()

  def pubb(self):
    Movement.pub.publish(Movement.move)
    #print(Movement.dx_a_1,Movement.dx_f_1,Movement.dx_t_1)
    Movement.rate.sleep()

  def avanti(self):
    Movement.z3=Movement.z
    if Movement.firstStep == 1:
      while Movement.z3<-80:
        #d=right a=coxa, f=femur, t=tibia
        Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z3)
        Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z3)
        Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z3)

        Movement.sx_a_1 =  Movement.dx_a_2
        Movement.sx_f_1 = -Movement.dx_f_2
        Movement.sx_t_1 = -Movement.dx_t_2

        Movement.sx_a_3 =  Movement.dx_a_2
        Movement.sx_f_3 = -Movement.dx_f_2
        Movement.sx_t_3 = -Movement.dx_t_2
            
        ophelia.moving()
        Movement.z3=Movement.z3+1
        ophelia.pubb()

    Movement.firstStep=0
    Movement.z1=Movement.z3
    Movement.z2=Movement.z3

    while Movement.y>-50:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y1, Movement.z)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y1, Movement.z)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y1, Movement.z)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z1)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z1)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z1)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1, Movement.z)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1, Movement.z)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1, Movement.z)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(-Movement.x2, Movement.y1, Movement.z2)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(-Movement.x2, Movement.y1, Movement.z2)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(-Movement.x2, Movement.y1, Movement.z2)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(-Movement.x1, Movement.y1, Movement.z2)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(-Movement.x1, Movement.y1, Movement.z2)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(-Movement.x1, Movement.y1, Movement.z2)

      ophelia.moving()
      Movement.y=Movement.y-1
      Movement.x1=Movement.x1-(1/math.sqrt(2))
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)
      ophelia.pubb()

    while Movement.y<50:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y1, Movement.z2)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y1, Movement.z2)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y1, Movement.z2)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1, Movement.z2)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1, Movement.z2)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1, Movement.z2)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(-Movement.x2, Movement.y1, Movement.z)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(-Movement.x2, Movement.y1, Movement.z)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(-Movement.x2, Movement.y1, Movement.z)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z1)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z1)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z1)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(-Movement.x1, Movement.y1, Movement.z)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(-Movement.x1, Movement.y1, Movement.z)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(-Movement.x1, Movement.y1, Movement.z)

      ophelia.moving()
      Movement.y=Movement.y+1
      Movement.x1=Movement.x1+(1/math.sqrt(2))
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)
      ophelia.pubb()

  def avantiUscita(self):
    Movement.firstStep=1
    while Movement.y>0:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y1, Movement.z)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y1, Movement.z)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y1, Movement.z)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z1)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z1)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z1)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1, Movement.z)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1, Movement.z)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1, Movement.z)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(-Movement.x2, Movement.y1, Movement.z2)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(-Movement.x2, Movement.y1, Movement.z2)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(-Movement.x2, Movement.y1, Movement.z2)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(-Movement.x1, Movement.y1, Movement.z2)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(-Movement.x1, Movement.y1, Movement.z2)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(-Movement.x1, Movement.y1, Movement.z2)

      ophelia.moving()
      Movement.y=Movement.y-1
      Movement.x1=Movement.x1-(1/math.sqrt(2))
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)
      ophelia.pubb()

    while Movement.z2>-130:
      #d=right a=coxa, f=femur, t=tibia
      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z2)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z2)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z2)

      Movement.sx_a_1 =  Movement.dx_a_2
      Movement.sx_f_1 = -Movement.dx_f_2
      Movement.sx_t_1 = -Movement.dx_t_2

      Movement.sx_a_3 =  Movement.dx_a_2
      Movement.sx_f_3 = -Movement.dx_f_2
      Movement.sx_t_3 = -Movement.dx_t_2
          
      ophelia.moving()
      Movement.z2=Movement.z2-1
      ophelia.pubb()

  def indietro(self):
    Movement.z3=Movement.z
    if Movement.firstStep == 1:
      while Movement.z3<-100:
        #d=right a=coxa, f=femur, t=tibia
        Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, -Movement.y, Movement.z3)
        Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, -Movement.y, Movement.z3)
        Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, -Movement.y, Movement.z3)

        Movement.sx_a_1 =  Movement.dx_a_2
        Movement.sx_f_1 = -Movement.dx_f_2
        Movement.sx_t_1 = -Movement.dx_t_2

        Movement.sx_a_3 =  Movement.dx_a_2
        Movement.sx_f_3 = -Movement.dx_f_2
        Movement.sx_t_3 = -Movement.dx_t_2
            
        ophelia.moving()
        Movement.z3=Movement.z3+1
        ophelia.pubb()

    Movement.firstStep=0
    Movement.z1=Movement.z3
    Movement.z2=Movement.z3

    while Movement.y>-50:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y1, Movement.z)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y1, Movement.z)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y1, Movement.z)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, -Movement.y, Movement.z1)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, -Movement.y, Movement.z1)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, -Movement.y, Movement.z1)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1, Movement.z)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1, Movement.z)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1, Movement.z)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(-Movement.x2, Movement.y1, Movement.z2)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(-Movement.x2, Movement.y1, Movement.z2)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(-Movement.x2, Movement.y1, Movement.z2)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x, -Movement.y, Movement.z)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x, -Movement.y, Movement.z)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x, -Movement.y, Movement.z)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(-Movement.x1, Movement.y1, Movement.z2)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(-Movement.x1, Movement.y1, Movement.z2)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(-Movement.x1, Movement.y1, Movement.z2)

      ophelia.moving()
      Movement.y=Movement.y-1
      Movement.x1=Movement.x1+(1/math.sqrt(2))
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)
      ophelia.pubb()

    while Movement.y<50:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y1, Movement.z2)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y1, Movement.z2)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y1, Movement.z2)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, -Movement.y, Movement.z)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, -Movement.y, Movement.z)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, -Movement.y, Movement.z)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1, Movement.z2)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1, Movement.z2)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1, Movement.z2)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(-Movement.x2, Movement.y1, Movement.z)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(-Movement.x2, Movement.y1, Movement.z)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(-Movement.x2, Movement.y1, Movement.z)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x, -Movement.y, Movement.z1)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x, -Movement.y, Movement.z1)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x, -Movement.y, Movement.z1)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(-Movement.x1, Movement.y1, Movement.z)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(-Movement.x1, Movement.y1, Movement.z)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(-Movement.x1, Movement.y1, Movement.z)

      ophelia.moving()
      Movement.y=Movement.y+1
      Movement.x1=Movement.x1-(1/math.sqrt(2))
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)
      ophelia.pubb()

  def indietroUscita(self):
    Movement.firstStep=1
    while Movement.y>0:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y1, Movement.z)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y1, Movement.z)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y1, Movement.z)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, -Movement.y, Movement.z1)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, -Movement.y, Movement.z1)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, -Movement.y, Movement.z1)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,Movement.y1, Movement.z)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,Movement.y1, Movement.z)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,Movement.y1, Movement.z)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(-Movement.x2, Movement.y1, Movement.z2)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(-Movement.x2, Movement.y1, Movement.z2)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(-Movement.x2, Movement.y1, Movement.z2)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x, -Movement.y, Movement.z)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x, -Movement.y, Movement.z)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x, -Movement.y, Movement.z)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(-Movement.x1, Movement.y1, Movement.z2)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(-Movement.x1, Movement.y1, Movement.z2)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(-Movement.x1, Movement.y1, Movement.z2)

      ophelia.moving()
      Movement.y=Movement.y-1
      Movement.x1=Movement.x1+(1/math.sqrt(2))
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=-Movement.x1+135
      Movement.z1=-(Movement.y*Movement.y*0.02+80)
      Movement.z2=-(Movement.y1*Movement.y1*0.0282843+80)
      ophelia.pubb()
      

    while Movement.z2>-130:
      #d=right a=coxa, f=femur, t=tibia
      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, -Movement.y, Movement.z2)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, -Movement.y, Movement.z2)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, -Movement.y, Movement.z2)

      Movement.sx_a_1 =  Movement.dx_a_2
      Movement.sx_f_1 = -Movement.dx_f_2
      Movement.sx_t_1 = -Movement.dx_t_2

      Movement.sx_a_3 =  Movement.dx_a_2
      Movement.sx_f_3 = -Movement.dx_f_2
      Movement.sx_t_3 = -Movement.dx_t_2
          
      ophelia.moving()
      Movement.z2=Movement.z2-1
      ophelia.pubb()

  def alza(self):
    while Movement.z>-130:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z)
      
      Movement.dx_a_2 =  Movement.dx_a_1
      Movement.dx_f_2 =  Movement.dx_f_1
      Movement.dx_t_2 =  Movement.dx_t_1

      Movement.dx_a_3 =  Movement.dx_a_1
      Movement.dx_f_3 =  Movement.dx_f_1
      Movement.dx_t_3 =  Movement.dx_t_1

      Movement.sx_a_1 =  Movement.dx_a_1
      Movement.sx_f_1 = -Movement.dx_f_1
      Movement.sx_t_1 = -Movement.dx_t_1

      Movement.sx_a_2 =  Movement.dx_a_1
      Movement.sx_f_2 = -Movement.dx_f_1
      Movement.sx_t_2 = -Movement.dx_t_1

      Movement.sx_a_3 =  Movement.dx_a_1
      Movement.sx_f_3 = -Movement.dx_f_1
      Movement.sx_t_3 = -Movement.dx_t_1
          
      ophelia.moving()
      Movement.z=Movement.z-1
      ophelia.pubb()

  def destra(self):
    Movement.z3=Movement.z
    if Movement.firstStep == 1:
      while Movement.z3<-100:
        #d=right a=coxa, f=femur, t=tibia
        Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z3)
        Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z3)
        Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z3)

        Movement.sx_a_1 =  Movement.dx_a_2
        Movement.sx_f_1 = -Movement.dx_f_2
        Movement.sx_t_1 = -Movement.dx_t_2

        Movement.sx_a_3 =  Movement.dx_a_2
        Movement.sx_f_3 = -Movement.dx_f_2
        Movement.sx_t_3 = -Movement.dx_t_2
            
        ophelia.moving()
        Movement.z3=Movement.z3+1
        ophelia.pubb()

    Movement.firstStep=0
    Movement.z1=Movement.z3
    Movement.z2=Movement.z3

    while Movement.x>95:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y, Movement.z1)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y, Movement.z1)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y, Movement.z1)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z1)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z1)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z1)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y, Movement.z)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y, Movement.z)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y, Movement.z)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z1)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z1)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z1)

      ophelia.moving()
      Movement.x=Movement.x-1
      Movement.x1=Movement.x1+1
      Movement.z1=-(Movement.x*Movement.x*0.01875+441.7-5.065*Movement.x)
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=Movement.y1-(1/math.sqrt(2))
      ophelia.pubb()

    while Movement.x<175:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z1)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z1)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z1)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y, Movement.z)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y, Movement.z)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y, Movement.z)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z1)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z1)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z1)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y, Movement.z1)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y, Movement.z1)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y, Movement.z1)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z)

      ophelia.moving()
      Movement.x=Movement.x+1
      Movement.x1=Movement.x1-1
      Movement.z1=-(Movement.x*Movement.x*0.01875+441.7-5.065*Movement.x)
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=Movement.y1+(1/math.sqrt(2))
      ophelia.pubb()

  def destraUscita(self):
    while Movement.x>135:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y, Movement.z1)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y, Movement.z1)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y, Movement.z1)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z1)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z1)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z1)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y, Movement.z)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y, Movement.z)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y, Movement.z)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z1)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z1)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z1)

      ophelia.moving()
      Movement.x=Movement.x-1
      Movement.x1=Movement.x1+1
      Movement.z1=-(Movement.x*Movement.x*0.01875+441.7-5.065*Movement.x)
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=Movement.y1-(1/math.sqrt(2))
      ophelia.pubb()

    while Movement.z2>-130:
      #d=right a=coxa, f=femur, t=tibia
      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z2)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z2)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z2)

      Movement.sx_a_1 =  Movement.dx_a_2
      Movement.sx_f_1 = -Movement.dx_f_2
      Movement.sx_t_1 = -Movement.dx_t_2

      Movement.sx_a_3 =  Movement.dx_a_2
      Movement.sx_f_3 = -Movement.dx_f_2
      Movement.sx_t_3 = -Movement.dx_t_2
          
      ophelia.moving()
      Movement.z2=Movement.z2-1
      ophelia.pubb()

  def sinistra(self):
    Movement.z3=Movement.z
    if Movement.firstStep == 1:
      while Movement.z3<-100:
        #d=right a=coxa, f=femur, t=tibia
        Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z3)
        Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z3)
        Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z3)

        Movement.sx_a_1 =  Movement.dx_a_2
        Movement.sx_f_1 = -Movement.dx_f_2
        Movement.sx_t_1 = -Movement.dx_t_2

        Movement.sx_a_3 =  Movement.dx_a_2
        Movement.sx_f_3 = -Movement.dx_f_2
        Movement.sx_t_3 = -Movement.dx_t_2
            
        ophelia.moving()
        Movement.z3=Movement.z3+1
        ophelia.pubb()

    Movement.firstStep=0
    Movement.z1=Movement.z3
    Movement.z2=Movement.z3

    while Movement.x<175:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y, Movement.z1)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y, Movement.z1)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y, Movement.z1)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z1)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z1)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z1)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y, Movement.z)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y, Movement.z)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y, Movement.z)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z1)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z1)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z1)

      ophelia.moving()
      Movement.x=Movement.x+1
      Movement.x1=Movement.x1-1
      Movement.z1=-(Movement.x*Movement.x*0.01875+441.7-5.065*Movement.x)
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=Movement.y1+(1/math.sqrt(2))
      ophelia.pubb()

    while Movement.x>95:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z1)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z1)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z1)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y, Movement.z)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y, Movement.z)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y, Movement.z)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z1)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z1)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z1)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y, Movement.z1)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y, Movement.z1)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y, Movement.z1)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z)

      ophelia.moving()
      Movement.x=Movement.x-1
      Movement.x1=Movement.x1+1
      Movement.z1=-(Movement.x*Movement.x*0.01875+441.7-5.065*Movement.x)
      Movement.x2=Movement.x2-(1/math.sqrt(2))
      Movement.y1=Movement.y1-(1/math.sqrt(2))
      ophelia.pubb()

  def sinistraUscita(self):
    while Movement.x<135:
      #destra destri a=anca, f=femore, t=tibia
      Movement.dx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z)
      Movement.dx_f_1 = Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z)
      Movement.dx_t_1 = Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z)

      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x1, Movement.y, Movement.z1)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x1, Movement.y, Movement.z1)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x1, Movement.y, Movement.z1)

      Movement.dx_a_3 =-Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z)
      Movement.dx_f_3 = Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z)
      Movement.dx_t_3 = Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z)

      Movement.sx_a_1 = Movement.braccio1.calcoloIK_joint1(Movement.x2, Movement.y1, Movement.z1)
      Movement.sx_f_1 =-Movement.braccio1.calcoloIK_joint2(Movement.x2, Movement.y1, Movement.z1)
      Movement.sx_t_1 =-Movement.braccio1.calcoloIK_joint3(Movement.x2, Movement.y1, Movement.z1)

      Movement.sx_a_2 =-Movement.braccio1.calcoloIK_joint1(Movement.x1,-Movement.y, Movement.z)
      Movement.sx_f_2 =-Movement.braccio1.calcoloIK_joint2(Movement.x1,-Movement.y, Movement.z)
      Movement.sx_t_2 =-Movement.braccio1.calcoloIK_joint3(Movement.x1,-Movement.y, Movement.z)

      Movement.sx_a_3 = Movement.braccio1.calcoloIK_joint1(Movement.x2,-Movement.y1, Movement.z1)
      Movement.sx_f_3 =-Movement.braccio1.calcoloIK_joint2(Movement.x2,-Movement.y1, Movement.z1)
      Movement.sx_t_3 =-Movement.braccio1.calcoloIK_joint3(Movement.x2,-Movement.y1, Movement.z1)

      ophelia.moving()
      Movement.x=Movement.x+1
      Movement.x1=Movement.x1-1
      Movement.z1=-(Movement.x*Movement.x*0.01875+441.7-5.065*Movement.x)
      Movement.x2=Movement.x2+(1/math.sqrt(2))
      Movement.y1=Movement.y1+(1/math.sqrt(2))
      ophelia.pubb()

    while Movement.z2>-130:
      #d=right a=coxa, f=femur, t=tibia
      Movement.dx_a_2 = Movement.braccio1.calcoloIK_joint1(Movement.x, Movement.y, Movement.z2)
      Movement.dx_f_2 = Movement.braccio1.calcoloIK_joint2(Movement.x, Movement.y, Movement.z2)
      Movement.dx_t_2 = Movement.braccio1.calcoloIK_joint3(Movement.x, Movement.y, Movement.z2)

      Movement.sx_a_1 =  Movement.dx_a_2
      Movement.sx_f_1 = -Movement.dx_f_2
      Movement.sx_t_1 = -Movement.dx_t_2

      Movement.sx_a_3 =  Movement.dx_a_2
      Movement.sx_f_3 = -Movement.dx_f_2
      Movement.sx_t_3 = -Movement.dx_t_2
          
      ophelia.moving()
      Movement.z2=Movement.z2-1
      ophelia.pubb()


ophelia=Movement()
ophelia.alza()
  

while not rospy.is_shutdown():
  #rospy.init_node('listener', anonymous=True)
  data=rospy.wait_for_message('/chatter', String)
  if data.data == "w":
    if Movement.dataOld==data.data:
      print("avanti")
      ophelia.avanti()
    elif Movement.dataOld=="x":
      print("indietroUscita")
      ophelia.indietroUscita()
    elif Movement.dataOld=="":
      print("avanti")
      ophelia.avanti()
    elif Movement.dataOld=="s":
      print("avanti")
      ophelia.avanti()
    elif Movement.dataOld=="a":
      print("sinistraUscita")
      ophelia.sinistraUscita()
    elif Movement.dataOld=="d":
      print("destraUscita")
      ophelia.destraUscita()
    else:
      print("avantiUscita")
      ophelia.avantiUscita()
  elif data.data == "x":
    if Movement.dataOld==data.data:
      print("indietro")
      ophelia.indietro()
    elif Movement.dataOld=="w":
      print("avantiUscita")
      ophelia.avantiUscita()
    elif Movement.dataOld=="":
      print("indietro")
      ophelia.indietro()
    elif Movement.dataOld=="s":
      print("indietro")
      ophelia.indietro()
    elif Movement.dataOld=="a":
      print("sinistraUscita")
      ophelia.sinistraUscita()
    elif Movement.dataOld=="d":
      print("destraUscita")
      ophelia.destraUscita()
    else:
      print("indietroUscita")
      ophelia.indietroUscita()
  elif data.data == "a":
    if Movement.dataOld==data.data:
      print("sinistra")
      ophelia.sinistra()
    elif Movement.dataOld=="w":
      print("avantiUscita")
      ophelia.avantiUscita()
    elif Movement.dataOld=="":
      print("sinistra")
      ophelia.sinistra()
    elif Movement.dataOld=="s":
      print("sinistraUscita")
      ophelia.sinistraUscita()
    elif Movement.dataOld=="x":
      print("indietroUscita")
      ophelia.indietroUscita()
    elif Movement.dataOld=="d":
      print("destraUscita")
      ophelia.destraUscita()
    else:
      print("sinistraUscita")
      ophelia.sinistraUscita()
  elif data.data == "d":
    if Movement.dataOld==data.data:
      print("destra")
      ophelia.destra()
    elif Movement.dataOld=="w":
      print("avantiUscita")
      ophelia.avantiUscita()
    elif Movement.dataOld=="":
      print("destra")
      ophelia.destra()
    elif Movement.dataOld=="s":
      print("sinistraUscita")
      ophelia.sinistra()
    elif Movement.dataOld=="x":
      print("indietroUscita")
      ophelia.indietroUscita()
    elif Movement.dataOld=="d":
      print("destraUscita")
      ophelia.destraUscita()
    else:
      print("destraUscita")
      ophelia.destraUscita()
  elif data.data == "s":
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
    
  Movement.dataOld=data.data

#ophelia.alza()
#ophelia.indietro()
#ophelia.avanti()
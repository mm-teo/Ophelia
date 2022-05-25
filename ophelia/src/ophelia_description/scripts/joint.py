#! /usr/bin/env python

import time
import math
from adafruit_servokit import ServoKit
from adafruit_servokit_2 import ServoKit2
from dictionary import Values
import keyboard
from bluedot import BlueDot
from signal import pause

class Movement:
  def __init__(self):
    pass
  step=4
  wait=0
  right = ServoKit(channels=16)
  left = ServoKit2(channels=16)
  dataOld='fermo'
  seduto=1

  def chiusura(self):
    traiettorie=Values()
    Movement.right.servo[2].angle = traiettorie.chiusura[0]
    Movement.right.servo[1].angle = traiettorie.chiusura[1]
    Movement.right.servo[0].angle = traiettorie.chiusura[2]

    Movement.right.servo[5].angle = traiettorie.chiusura[3]
    Movement.right.servo[6].angle = traiettorie.chiusura[4]
    Movement.right.servo[7].angle = traiettorie.chiusura[5]

    Movement.right.servo[13].angle = traiettorie.chiusura[6]
    Movement.right.servo[14].angle = traiettorie.chiusura[7]
    Movement.right.servo[15].angle = traiettorie.chiusura[8]

    Movement.left.servo[13].angle = traiettorie.chiusura[9]
    Movement.left.servo[14].angle = traiettorie.chiusura[10]
    Movement.left.servo[15].angle = traiettorie.chiusura[11]

    Movement.left.servo[5].angle = traiettorie.chiusura[12]
    Movement.left.servo[6].angle = traiettorie.chiusura[13]
    Movement.left.servo[7].angle = traiettorie.chiusura[14]

    Movement.left.servo[2].angle = traiettorie.chiusura[15]
    Movement.left.servo[1].angle = traiettorie.chiusura[16]
    Movement.left.servo[0].angle = traiettorie.chiusura[17]

  def alzata(self):
    i=0
    traiettorie=Values()
    while i<99:
      Movement.right.servo[2].angle = traiettorie.alzata[i][0]
      Movement.right.servo[1].angle = traiettorie.alzata[i][1]
      Movement.right.servo[0].angle = traiettorie.alzata[i][2]

      Movement.right.servo[5].angle = traiettorie.alzata[i][3]
      Movement.right.servo[6].angle = traiettorie.alzata[i][4]
      Movement.right.servo[7].angle = traiettorie.alzata[i][5]

      Movement.right.servo[13].angle = traiettorie.alzata[i][6]
      Movement.right.servo[14].angle = traiettorie.alzata[i][7]
      Movement.right.servo[15].angle = traiettorie.alzata[i][8]

      Movement.left.servo[13].angle = traiettorie.alzata[i][9]
      Movement.left.servo[14].angle = traiettorie.alzata[i][10]
      Movement.left.servo[15].angle = traiettorie.alzata[i][11]

      Movement.left.servo[5].angle = traiettorie.alzata[i][12]
      Movement.left.servo[6].angle = traiettorie.alzata[i][13]
      Movement.left.servo[7].angle = traiettorie.alzata[i][14]

      Movement.left.servo[2].angle = traiettorie.alzata[i][15]
      Movement.left.servo[1].angle = traiettorie.alzata[i][16]
      Movement.left.servo[0].angle = traiettorie.alzata[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def seduta(self):
    i=0
    traiettorie=Values()
    while i<99:
      Movement.right.servo[2].angle = traiettorie.seduta[i][0]
      Movement.right.servo[1].angle = traiettorie.seduta[i][1]
      Movement.right.servo[0].angle = traiettorie.seduta[i][2]

      Movement.right.servo[5].angle = traiettorie.seduta[i][3]
      Movement.right.servo[6].angle = traiettorie.seduta[i][4]
      Movement.right.servo[7].angle = traiettorie.seduta[i][5]

      Movement.right.servo[13].angle = traiettorie.seduta[i][6]
      Movement.right.servo[14].angle = traiettorie.seduta[i][7]
      Movement.right.servo[15].angle = traiettorie.seduta[i][8]

      Movement.left.servo[13].angle = traiettorie.seduta[i][9]
      Movement.left.servo[14].angle = traiettorie.seduta[i][10]
      Movement.left.servo[15].angle = traiettorie.seduta[i][11]

      Movement.left.servo[5].angle = traiettorie.seduta[i][12]
      Movement.left.servo[6].angle = traiettorie.seduta[i][13]
      Movement.left.servo[7].angle = traiettorie.seduta[i][14]

      Movement.left.servo[2].angle = traiettorie.seduta[i][15]
      Movement.left.servo[1].angle = traiettorie.seduta[i][16]
      Movement.left.servo[0].angle = traiettorie.seduta[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def avantiIngresso(self):
    i=0
    traiettorie=Values()
    while i<50:
      Movement.right.servo[2].angle = traiettorie.avantiIngresso[i][0]
      Movement.right.servo[1].angle = traiettorie.avantiIngresso[i][1]
      Movement.right.servo[0].angle = traiettorie.avantiIngresso[i][2]

      Movement.right.servo[5].angle = traiettorie.avantiIngresso[i][3]
      Movement.right.servo[6].angle = traiettorie.avantiIngresso[i][4]
      Movement.right.servo[7].angle = traiettorie.avantiIngresso[i][5]

      Movement.right.servo[13].angle = traiettorie.avantiIngresso[i][6]
      Movement.right.servo[14].angle = traiettorie.avantiIngresso[i][7]
      Movement.right.servo[15].angle = traiettorie.avantiIngresso[i][8]

      Movement.left.servo[13].angle = traiettorie.avantiIngresso[i][9]
      Movement.left.servo[14].angle = traiettorie.avantiIngresso[i][10]
      Movement.left.servo[15].angle = traiettorie.avantiIngresso[i][11]

      Movement.left.servo[5].angle = traiettorie.avantiIngresso[i][12]
      Movement.left.servo[6].angle = traiettorie.avantiIngresso[i][13]
      Movement.left.servo[7].angle = traiettorie.avantiIngresso[i][14]

      Movement.left.servo[2].angle = traiettorie.avantiIngresso[i][15]
      Movement.left.servo[1].angle = traiettorie.avantiIngresso[i][16]
      Movement.left.servo[0].angle = traiettorie.avantiIngresso[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def avanti(self):
    i=0
    traiettorie=Values()
    while i<150:
      Movement.right.servo[2].angle = traiettorie.avanti[i][0]
      Movement.right.servo[1].angle = traiettorie.avanti[i][1]
      Movement.right.servo[0].angle = traiettorie.avanti[i][2]

      Movement.right.servo[5].angle = traiettorie.avanti[i][3]
      Movement.right.servo[6].angle = traiettorie.avanti[i][4]
      Movement.right.servo[7].angle = traiettorie.avanti[i][5]

      Movement.right.servo[13].angle = traiettorie.avanti[i][6]
      Movement.right.servo[14].angle = traiettorie.avanti[i][7]
      Movement.right.servo[15].angle = traiettorie.avanti[i][8]

      Movement.left.servo[13].angle = traiettorie.avanti[i][9]
      Movement.left.servo[14].angle = traiettorie.avanti[i][10]
      Movement.left.servo[15].angle = traiettorie.avanti[i][11]

      Movement.left.servo[5].angle = traiettorie.avanti[i][12]
      Movement.left.servo[6].angle = traiettorie.avanti[i][13]
      Movement.left.servo[7].angle = traiettorie.avanti[i][14]

      Movement.left.servo[2].angle = traiettorie.avanti[i][15]
      Movement.left.servo[1].angle = traiettorie.avanti[i][16]
      Movement.left.servo[0].angle = traiettorie.avanti[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def avantiUscita(self):
    i=0
    traiettorie=Values()
    while i<100:
      Movement.right.servo[2].angle = traiettorie.avantiUscita[i][0]
      Movement.right.servo[1].angle = traiettorie.avantiUscita[i][1]
      Movement.right.servo[0].angle = traiettorie.avantiUscita[i][2]

      Movement.right.servo[5].angle = traiettorie.avantiUscita[i][3]
      Movement.right.servo[6].angle = traiettorie.avantiUscita[i][4]
      Movement.right.servo[7].angle = traiettorie.avantiUscita[i][5]

      Movement.right.servo[13].angle = traiettorie.avantiUscita[i][6]
      Movement.right.servo[14].angle = traiettorie.avantiUscita[i][7]
      Movement.right.servo[15].angle = traiettorie.avantiUscita[i][8]

      Movement.left.servo[13].angle = traiettorie.avantiUscita[i][9]
      Movement.left.servo[14].angle = traiettorie.avantiUscita[i][10]
      Movement.left.servo[15].angle = traiettorie.avantiUscita[i][11]

      Movement.left.servo[5].angle = traiettorie.avantiUscita[i][12]
      Movement.left.servo[6].angle = traiettorie.avantiUscita[i][13]
      Movement.left.servo[7].angle = traiettorie.avantiUscita[i][14]

      Movement.left.servo[2].angle = traiettorie.avantiUscita[i][15]
      Movement.left.servo[1].angle = traiettorie.avantiUscita[i][16]
      Movement.left.servo[0].angle = traiettorie.avantiUscita[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def indietroIngresso(self):
    i=0
    traiettorie=Values()
    while i<50:
      Movement.right.servo[2].angle = traiettorie.indietroIngresso[i][0]
      Movement.right.servo[1].angle = traiettorie.indietroIngresso[i][1]
      Movement.right.servo[0].angle = traiettorie.indietroIngresso[i][2]

      Movement.right.servo[5].angle = traiettorie.indietroIngresso[i][3]
      Movement.right.servo[6].angle = traiettorie.indietroIngresso[i][4]
      Movement.right.servo[7].angle = traiettorie.indietroIngresso[i][5]

      Movement.right.servo[13].angle = traiettorie.indietroIngresso[i][6]
      Movement.right.servo[14].angle = traiettorie.indietroIngresso[i][7]
      Movement.right.servo[15].angle = traiettorie.indietroIngresso[i][8]

      Movement.left.servo[13].angle = traiettorie.indietroIngresso[i][9]
      Movement.left.servo[14].angle = traiettorie.indietroIngresso[i][10]
      Movement.left.servo[15].angle = traiettorie.indietroIngresso[i][11]

      Movement.left.servo[5].angle = traiettorie.indietroIngresso[i][12]
      Movement.left.servo[6].angle = traiettorie.indietroIngresso[i][13]
      Movement.left.servo[7].angle = traiettorie.indietroIngresso[i][14]

      Movement.left.servo[2].angle = traiettorie.indietroIngresso[i][15]
      Movement.left.servo[1].angle = traiettorie.indietroIngresso[i][16]
      Movement.left.servo[0].angle = traiettorie.indietroIngresso[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def indietro(self):
    i=0
    traiettorie=Values()
    while i<150:
      Movement.right.servo[2].angle = traiettorie.indietro[i][0]
      Movement.right.servo[1].angle = traiettorie.indietro[i][1]
      Movement.right.servo[0].angle = traiettorie.indietro[i][2]

      Movement.right.servo[5].angle = traiettorie.indietro[i][3]
      Movement.right.servo[6].angle = traiettorie.indietro[i][4]
      Movement.right.servo[7].angle = traiettorie.indietro[i][5]

      Movement.right.servo[13].angle = traiettorie.indietro[i][6]
      Movement.right.servo[14].angle = traiettorie.indietro[i][7]
      Movement.right.servo[15].angle = traiettorie.indietro[i][8]

      Movement.left.servo[13].angle = traiettorie.indietro[i][9]
      Movement.left.servo[14].angle = traiettorie.indietro[i][10]
      Movement.left.servo[15].angle = traiettorie.indietro[i][11]

      Movement.left.servo[5].angle = traiettorie.indietro[i][12]
      Movement.left.servo[6].angle = traiettorie.indietro[i][13]
      Movement.left.servo[7].angle = traiettorie.indietro[i][14]

      Movement.left.servo[2].angle = traiettorie.indietro[i][15]
      Movement.left.servo[1].angle = traiettorie.indietro[i][16]
      Movement.left.servo[0].angle = traiettorie.indietro[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)
  
  def indietroUscita(self):
    i=0
    traiettorie=Values()
    while i<100:
      Movement.right.servo[2].angle = traiettorie.indietroUscita[i][0]
      Movement.right.servo[1].angle = traiettorie.indietroUscita[i][1]
      Movement.right.servo[0].angle = traiettorie.indietroUscita[i][2]

      Movement.right.servo[5].angle = traiettorie.indietroUscita[i][3]
      Movement.right.servo[6].angle = traiettorie.indietroUscita[i][4]
      Movement.right.servo[7].angle = traiettorie.indietroUscita[i][5]

      Movement.right.servo[13].angle = traiettorie.indietroUscita[i][6]
      Movement.right.servo[14].angle = traiettorie.indietroUscita[i][7]
      Movement.right.servo[15].angle = traiettorie.indietroUscita[i][8]

      Movement.left.servo[13].angle = traiettorie.indietroUscita[i][9]
      Movement.left.servo[14].angle = traiettorie.indietroUscita[i][10]
      Movement.left.servo[15].angle = traiettorie.indietroUscita[i][11]

      Movement.left.servo[5].angle = traiettorie.indietroUscita[i][12]
      Movement.left.servo[6].angle = traiettorie.indietroUscita[i][13]
      Movement.left.servo[7].angle = traiettorie.indietroUscita[i][14]

      Movement.left.servo[2].angle = traiettorie.indietroUscita[i][15]
      Movement.left.servo[1].angle = traiettorie.indietroUscita[i][16]
      Movement.left.servo[0].angle = traiettorie.indietroUscita[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def destraIngresso(self):
    i=0
    traiettorie=Values()
    while i<50:
      Movement.right.servo[2].angle = traiettorie.destraIngresso[i][0]
      Movement.right.servo[1].angle = traiettorie.destraIngresso[i][1]
      Movement.right.servo[0].angle = traiettorie.destraIngresso[i][2]

      Movement.right.servo[5].angle = traiettorie.destraIngresso[i][3]
      Movement.right.servo[6].angle = traiettorie.destraIngresso[i][4]
      Movement.right.servo[7].angle = traiettorie.destraIngresso[i][5]

      Movement.right.servo[13].angle = traiettorie.destraIngresso[i][6]
      Movement.right.servo[14].angle = traiettorie.destraIngresso[i][7]
      Movement.right.servo[15].angle = traiettorie.destraIngresso[i][8]

      Movement.left.servo[13].angle = traiettorie.destraIngresso[i][9]
      Movement.left.servo[14].angle = traiettorie.destraIngresso[i][10]
      Movement.left.servo[15].angle = traiettorie.destraIngresso[i][11]

      Movement.left.servo[5].angle = traiettorie.destraIngresso[i][12]
      Movement.left.servo[6].angle = traiettorie.destraIngresso[i][13]
      Movement.left.servo[7].angle = traiettorie.destraIngresso[i][14]

      Movement.left.servo[2].angle = traiettorie.destraIngresso[i][15]
      Movement.left.servo[1].angle = traiettorie.destraIngresso[i][16]
      Movement.left.servo[0].angle = traiettorie.destraIngresso[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def destra(self):
    i=0
    traiettorie=Values()
    while i<150:
      Movement.right.servo[2].angle = traiettorie.destra[i][0]
      Movement.right.servo[1].angle = traiettorie.destra[i][1]
      Movement.right.servo[0].angle = traiettorie.destra[i][2]

      Movement.right.servo[5].angle = traiettorie.destra[i][3]
      Movement.right.servo[6].angle = traiettorie.destra[i][4]
      Movement.right.servo[7].angle = traiettorie.destra[i][5]

      Movement.right.servo[13].angle = traiettorie.destra[i][6]
      Movement.right.servo[14].angle = traiettorie.destra[i][7]
      Movement.right.servo[15].angle = traiettorie.destra[i][8]

      Movement.left.servo[13].angle = traiettorie.destra[i][9]
      Movement.left.servo[14].angle = traiettorie.destra[i][10]
      Movement.left.servo[15].angle = traiettorie.destra[i][11]

      Movement.left.servo[5].angle = traiettorie.destra[i][12]
      Movement.left.servo[6].angle = traiettorie.destra[i][13]
      Movement.left.servo[7].angle = traiettorie.destra[i][14]

      Movement.left.servo[2].angle = traiettorie.destra[i][15]
      Movement.left.servo[1].angle = traiettorie.destra[i][16]
      Movement.left.servo[0].angle = traiettorie.destra[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def destraUscita(self):
    i=0
    traiettorie=Values()
    while i<100:
      Movement.right.servo[2].angle = traiettorie.destraUscita[i][0]
      Movement.right.servo[1].angle = traiettorie.destraUscita[i][1]
      Movement.right.servo[0].angle = traiettorie.destraUscita[i][2]

      Movement.right.servo[5].angle = traiettorie.destraUscita[i][3]
      Movement.right.servo[6].angle = traiettorie.destraUscita[i][4]
      Movement.right.servo[7].angle = traiettorie.destraUscita[i][5]

      Movement.right.servo[13].angle = traiettorie.destraUscita[i][6]
      Movement.right.servo[14].angle = traiettorie.destraUscita[i][7]
      Movement.right.servo[15].angle = traiettorie.destraUscita[i][8]

      Movement.left.servo[13].angle = traiettorie.destraUscita[i][9]
      Movement.left.servo[14].angle = traiettorie.destraUscita[i][10]
      Movement.left.servo[15].angle = traiettorie.destraUscita[i][11]

      Movement.left.servo[5].angle = traiettorie.destraUscita[i][12]
      Movement.left.servo[6].angle = traiettorie.destraUscita[i][13]
      Movement.left.servo[7].angle = traiettorie.destraUscita[i][14]

      Movement.left.servo[2].angle = traiettorie.destraUscita[i][15]
      Movement.left.servo[1].angle = traiettorie.destraUscita[i][16]
      Movement.left.servo[0].angle = traiettorie.destraUscita[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def sinistraIngresso(self):
    i=0
    traiettorie=Values()
    while i<50:
      Movement.right.servo[2].angle = traiettorie.sinistraIngresso[i][0]
      Movement.right.servo[1].angle = traiettorie.sinistraIngresso[i][1]
      Movement.right.servo[0].angle = traiettorie.sinistraIngresso[i][2]

      Movement.right.servo[5].angle = traiettorie.sinistraIngresso[i][3]
      Movement.right.servo[6].angle = traiettorie.sinistraIngresso[i][4]
      Movement.right.servo[7].angle = traiettorie.sinistraIngresso[i][5]

      Movement.right.servo[13].angle = traiettorie.sinistraIngresso[i][6]
      Movement.right.servo[14].angle = traiettorie.sinistraIngresso[i][7]
      Movement.right.servo[15].angle = traiettorie.sinistraIngresso[i][8]

      Movement.left.servo[13].angle = traiettorie.sinistraIngresso[i][9]
      Movement.left.servo[14].angle = traiettorie.sinistraIngresso[i][10]
      Movement.left.servo[15].angle = traiettorie.sinistraIngresso[i][11]

      Movement.left.servo[5].angle = traiettorie.sinistraIngresso[i][12]
      Movement.left.servo[6].angle = traiettorie.sinistraIngresso[i][13]
      Movement.left.servo[7].angle = traiettorie.sinistraIngresso[i][14]

      Movement.left.servo[2].angle = traiettorie.sinistraIngresso[i][15]
      Movement.left.servo[1].angle = traiettorie.sinistraIngresso[i][16]
      Movement.left.servo[0].angle = traiettorie.sinistraIngresso[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def sinistra(self):
    i=0
    traiettorie=Values()
    while i<150:
      Movement.right.servo[2].angle = traiettorie.sinistra[i][0]
      Movement.right.servo[1].angle = traiettorie.sinistra[i][1]
      Movement.right.servo[0].angle = traiettorie.sinistra[i][2]

      Movement.right.servo[5].angle = traiettorie.sinistra[i][3]
      Movement.right.servo[6].angle = traiettorie.sinistra[i][4]
      Movement.right.servo[7].angle = traiettorie.sinistra[i][5]

      Movement.right.servo[13].angle = traiettorie.sinistra[i][6]
      Movement.right.servo[14].angle = traiettorie.sinistra[i][7]
      Movement.right.servo[15].angle = traiettorie.sinistra[i][8]

      Movement.left.servo[13].angle = traiettorie.sinistra[i][9]
      Movement.left.servo[14].angle = traiettorie.sinistra[i][10]
      Movement.left.servo[15].angle = traiettorie.sinistra[i][11]

      Movement.left.servo[5].angle = traiettorie.sinistra[i][12]
      Movement.left.servo[6].angle = traiettorie.sinistra[i][13]
      Movement.left.servo[7].angle = traiettorie.sinistra[i][14]

      Movement.left.servo[2].angle = traiettorie.sinistra[i][15]
      Movement.left.servo[1].angle = traiettorie.sinistra[i][16]
      Movement.left.servo[0].angle = traiettorie.sinistra[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def sinistraUscita(self):
    i=0
    traiettorie=Values()
    while i<100:
      Movement.right.servo[2].angle = traiettorie.sinistraUscita[i][0]
      Movement.right.servo[1].angle = traiettorie.sinistraUscita[i][1]
      Movement.right.servo[0].angle = traiettorie.sinistraUscita[i][2]

      Movement.right.servo[5].angle = traiettorie.sinistraUscita[i][3]
      Movement.right.servo[6].angle = traiettorie.sinistraUscita[i][4]
      Movement.right.servo[7].angle = traiettorie.sinistraUscita[i][5]

      Movement.right.servo[13].angle = traiettorie.sinistraUscita[i][6]
      Movement.right.servo[14].angle = traiettorie.sinistraUscita[i][7]
      Movement.right.servo[15].angle = traiettorie.sinistraUscita[i][8]

      Movement.left.servo[13].angle = traiettorie.sinistraUscita[i][9]
      Movement.left.servo[14].angle = traiettorie.sinistraUscita[i][10]
      Movement.left.servo[15].angle = traiettorie.sinistraUscita[i][11]

      Movement.left.servo[5].angle = traiettorie.sinistraUscita[i][12]
      Movement.left.servo[6].angle = traiettorie.sinistraUscita[i][13]
      Movement.left.servo[7].angle = traiettorie.sinistraUscita[i][14]

      Movement.left.servo[2].angle = traiettorie.sinistraUscita[i][15]
      Movement.left.servo[1].angle = traiettorie.sinistraUscita[i][16]
      Movement.left.servo[0].angle = traiettorie.sinistraUscita[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def ruotaDestraIngresso(self):
    i=0
    traiettorie=Values()
    while i<49:
      Movement.right.servo[2].angle = traiettorie.ruotaDestraIngresso[i][0]
      Movement.right.servo[1].angle = traiettorie.ruotaDestraIngresso[i][1]
      Movement.right.servo[0].angle = traiettorie.ruotaDestraIngresso[i][2]

      Movement.right.servo[5].angle = traiettorie.ruotaDestraIngresso[i][3]
      Movement.right.servo[6].angle = traiettorie.ruotaDestraIngresso[i][4]
      Movement.right.servo[7].angle = traiettorie.ruotaDestraIngresso[i][5]

      Movement.right.servo[13].angle = traiettorie.ruotaDestraIngresso[i][6]
      Movement.right.servo[14].angle = traiettorie.ruotaDestraIngresso[i][7]
      Movement.right.servo[15].angle = traiettorie.ruotaDestraIngresso[i][8]

      Movement.left.servo[13].angle = traiettorie.ruotaDestraIngresso[i][9]
      Movement.left.servo[14].angle = traiettorie.ruotaDestraIngresso[i][10]
      Movement.left.servo[15].angle = traiettorie.ruotaDestraIngresso[i][11]

      Movement.left.servo[5].angle = traiettorie.ruotaDestraIngresso[i][12]
      Movement.left.servo[6].angle = traiettorie.ruotaDestraIngresso[i][13]
      Movement.left.servo[7].angle = traiettorie.ruotaDestraIngresso[i][14]

      Movement.left.servo[2].angle = traiettorie.ruotaDestraIngresso[i][15]
      Movement.left.servo[1].angle = traiettorie.ruotaDestraIngresso[i][16]
      Movement.left.servo[0].angle = traiettorie.ruotaDestraIngresso[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def ruotaDestra(self):
    i=0
    traiettorie=Values()
    while i<155:
      Movement.right.servo[2].angle = traiettorie.ruotaDestra[i][0]
      Movement.right.servo[1].angle = traiettorie.ruotaDestra[i][1]
      Movement.right.servo[0].angle = traiettorie.ruotaDestra[i][2]

      Movement.right.servo[5].angle = traiettorie.ruotaDestra[i][3]
      Movement.right.servo[6].angle = traiettorie.ruotaDestra[i][4]
      Movement.right.servo[7].angle = traiettorie.ruotaDestra[i][5]

      Movement.right.servo[13].angle = traiettorie.ruotaDestra[i][6]
      Movement.right.servo[14].angle = traiettorie.ruotaDestra[i][7]
      Movement.right.servo[15].angle = traiettorie.ruotaDestra[i][8]

      Movement.left.servo[13].angle = traiettorie.ruotaDestra[i][9]
      Movement.left.servo[14].angle = traiettorie.ruotaDestra[i][10]
      Movement.left.servo[15].angle = traiettorie.ruotaDestra[i][11]

      Movement.left.servo[5].angle = traiettorie.ruotaDestra[i][12]
      Movement.left.servo[6].angle = traiettorie.ruotaDestra[i][13]
      Movement.left.servo[7].angle = traiettorie.ruotaDestra[i][14]

      Movement.left.servo[2].angle = traiettorie.ruotaDestra[i][15]
      Movement.left.servo[1].angle = traiettorie.ruotaDestra[i][16]
      Movement.left.servo[0].angle = traiettorie.ruotaDestra[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)
  
  def ruotaDestraUscita(self):
    i=0
    traiettorie=Values()
    while i<101:
      Movement.right.servo[2].angle = traiettorie.ruotaDestraUscita[i][0]
      Movement.right.servo[1].angle = traiettorie.ruotaDestraUscita[i][1]
      Movement.right.servo[0].angle = traiettorie.ruotaDestraUscita[i][2]

      Movement.right.servo[5].angle = traiettorie.ruotaDestraUscita[i][3]
      Movement.right.servo[6].angle = traiettorie.ruotaDestraUscita[i][4]
      Movement.right.servo[7].angle = traiettorie.ruotaDestraUscita[i][5]

      Movement.right.servo[13].angle = traiettorie.ruotaDestraUscita[i][6]
      Movement.right.servo[14].angle = traiettorie.ruotaDestraUscita[i][7]
      Movement.right.servo[15].angle = traiettorie.ruotaDestraUscita[i][8]

      Movement.left.servo[13].angle = traiettorie.ruotaDestraUscita[i][9]
      Movement.left.servo[14].angle = traiettorie.ruotaDestraUscita[i][10]
      Movement.left.servo[15].angle = traiettorie.ruotaDestraUscita[i][11]

      Movement.left.servo[5].angle = traiettorie.ruotaDestraUscita[i][12]
      Movement.left.servo[6].angle = traiettorie.ruotaDestraUscita[i][13]
      Movement.left.servo[7].angle = traiettorie.ruotaDestraUscita[i][14]

      Movement.left.servo[2].angle = traiettorie.ruotaDestraUscita[i][15]
      Movement.left.servo[1].angle = traiettorie.ruotaDestraUscita[i][16]
      Movement.left.servo[0].angle = traiettorie.ruotaDestraUscita[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def ruotaSinistraIngresso(self):
    i=0
    traiettorie=Values()
    while i<49:
      Movement.right.servo[2].angle = traiettorie.ruotaSinistraIngresso[i][0]
      Movement.right.servo[1].angle = traiettorie.ruotaSinistraIngresso[i][1]
      Movement.right.servo[0].angle = traiettorie.ruotaSinistraIngresso[i][2]

      Movement.right.servo[5].angle = traiettorie.ruotaSinistraIngresso[i][3]
      Movement.right.servo[6].angle = traiettorie.ruotaSinistraIngresso[i][4]
      Movement.right.servo[7].angle = traiettorie.ruotaSinistraIngresso[i][5]

      Movement.right.servo[13].angle = traiettorie.ruotaSinistraIngresso[i][6]
      Movement.right.servo[14].angle = traiettorie.ruotaSinistraIngresso[i][7]
      Movement.right.servo[15].angle = traiettorie.ruotaSinistraIngresso[i][8]

      Movement.left.servo[13].angle = traiettorie.ruotaSinistraIngresso[i][9]
      Movement.left.servo[14].angle = traiettorie.ruotaSinistraIngresso[i][10]
      Movement.left.servo[15].angle = traiettorie.ruotaSinistraIngresso[i][11]

      Movement.left.servo[5].angle = traiettorie.ruotaSinistraIngresso[i][12]
      Movement.left.servo[6].angle = traiettorie.ruotaSinistraIngresso[i][13]
      Movement.left.servo[7].angle = traiettorie.ruotaSinistraIngresso[i][14]

      Movement.left.servo[2].angle = traiettorie.ruotaSinistraIngresso[i][15]
      Movement.left.servo[1].angle = traiettorie.ruotaSinistraIngresso[i][16]
      Movement.left.servo[0].angle = traiettorie.ruotaSinistraIngresso[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def ruotaSinistra(self):
    i=0
    traiettorie=Values()
    while i<155:
      Movement.right.servo[2].angle = traiettorie.ruotaSinistra[i][0]
      Movement.right.servo[1].angle = traiettorie.ruotaSinistra[i][1]
      Movement.right.servo[0].angle = traiettorie.ruotaSinistra[i][2]

      Movement.right.servo[5].angle = traiettorie.ruotaSinistra[i][3]
      Movement.right.servo[6].angle = traiettorie.ruotaSinistra[i][4]
      Movement.right.servo[7].angle = traiettorie.ruotaSinistra[i][5]

      Movement.right.servo[13].angle = traiettorie.ruotaSinistra[i][6]
      Movement.right.servo[14].angle = traiettorie.ruotaSinistra[i][7]
      Movement.right.servo[15].angle = traiettorie.ruotaSinistra[i][8]

      Movement.left.servo[13].angle = traiettorie.ruotaSinistra[i][9]
      Movement.left.servo[14].angle = traiettorie.ruotaSinistra[i][10]
      Movement.left.servo[15].angle = traiettorie.ruotaSinistra[i][11]

      Movement.left.servo[5].angle = traiettorie.ruotaSinistra[i][12]
      Movement.left.servo[6].angle = traiettorie.ruotaSinistra[i][13]
      Movement.left.servo[7].angle = traiettorie.ruotaSinistra[i][14]

      Movement.left.servo[2].angle = traiettorie.ruotaSinistra[i][15]
      Movement.left.servo[1].angle = traiettorie.ruotaSinistra[i][16]
      Movement.left.servo[0].angle = traiettorie.ruotaSinistra[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

  def ruotaSinistraUscita(self):
    i=0
    traiettorie=Values()
    while i<101:
      Movement.right.servo[2].angle = traiettorie.ruotaSinistraUscita[i][0]
      Movement.right.servo[1].angle = traiettorie.ruotaSinistraUscita[i][1]
      Movement.right.servo[0].angle = traiettorie.ruotaSinistraUscita[i][2]

      Movement.right.servo[5].angle = traiettorie.ruotaSinistraUscita[i][3]
      Movement.right.servo[6].angle = traiettorie.ruotaSinistraUscita[i][4]
      Movement.right.servo[7].angle = traiettorie.ruotaSinistraUscita[i][5]

      Movement.right.servo[13].angle = traiettorie.ruotaSinistraUscita[i][6]
      Movement.right.servo[14].angle = traiettorie.ruotaSinistraUscita[i][7]
      Movement.right.servo[15].angle = traiettorie.ruotaSinistraUscita[i][8]

      Movement.left.servo[13].angle = traiettorie.ruotaSinistraUscita[i][9]
      Movement.left.servo[14].angle = traiettorie.ruotaSinistraUscita[i][10]
      Movement.left.servo[15].angle = traiettorie.ruotaSinistraUscita[i][11]

      Movement.left.servo[5].angle = traiettorie.ruotaSinistraUscita[i][12]
      Movement.left.servo[6].angle = traiettorie.ruotaSinistraUscita[i][13]
      Movement.left.servo[7].angle = traiettorie.ruotaSinistraUscita[i][14]

      Movement.left.servo[2].angle = traiettorie.ruotaSinistraUscita[i][15]
      Movement.left.servo[1].angle = traiettorie.ruotaSinistraUscita[i][16]
      Movement.left.servo[0].angle = traiettorie.ruotaSinistraUscita[i][17]
      i=i+Movement.step
      time.sleep(Movement.wait)

ophelia=Movement()
ophelia.chiusura()
Movement.seduto=1


def up():
  if Movement.seduto==0:
    if Movement.dataOld=='fermo' or Movement.dataOld=='avanti':
      print("avanti")
      ophelia.avantiIngresso()
      ophelia.avanti()
      Movement.dataOld='avanti'
    elif Movement.dataOld=='indietro':
      ophelia.indietroUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='destra':
      ophelia.destraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='sinistra':
      ophelia.sinistraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotasx':
      ophelia.ruotaSinistraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotadx':
      ophelia.ruotaDestraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='stop':
      ophelia.avantiUscita()
      Movement.dataOld='fermo'

def down():
  if Movement.seduto==0:
    if Movement.dataOld=='fermo' or Movement.dataOld=='indietro':
      print("indietro")
      ophelia.indietroIngresso()
      ophelia.indietro()
      Movement.dataOld='indietro'
    elif Movement.dataOld=='avanti':
      ophelia.avantiUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='destra':
      ophelia.destraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='sinistra':
      ophelia.sinistraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotasx':
      ophelia.ruotaSinistraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotadx':
      ophelia.ruotaDestraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='stop':
      ophelia.indietroUscita()
      Movement.dataOld='fermo'

def left():
  if Movement.seduto==0:
    if Movement.dataOld=='fermo' or Movement.dataOld=='sinistra':
      print("sinistra")
      ophelia.sinistraIngresso()
      ophelia.sinistra()
      Movement.dataOld='sinistra'
    elif Movement.dataOld=='avanti':
      ophelia.avantiUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='destra':
      ophelia.destraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='indietro':
      ophelia.indietroUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotasx':
      ophelia.ruotaSinistraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotadx':
      ophelia.ruotaDestraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='stop':
      ophelia.sinistraUscita()
      Movement.dataOld='fermo'

def right():
  if Movement.seduto==0:
    if Movement.dataOld=='fermo' or Movement.dataOld=='destra':
      print("destra")
      ophelia.destraIngresso()
      ophelia.destra()
      Movement.dataOld='destra'
    elif Movement.dataOld=='indietro':
      ophelia.indietroUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='avanti':
      ophelia.avantiUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='sinistra':
      ophelia.sinistraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotasx':
      ophelia.ruotaSinistraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotadx':
      ophelia.ruotaDestraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='stop':
      ophelia.avantiUscita()
      Movement.dataOld='fermo'

def turnLeft():
  if Movement.seduto==0:
    if Movement.dataOld=='fermo' or Movement.dataOld=='ruotasx':
      print("ruotasx")
      ophelia.ruotaSinistraIngresso()
      ophelia.ruotaSinistra()
      Movement.dataOld='ruotasx'
    elif Movement.dataOld=='indietro':
      ophelia.indietroUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='destra':
      ophelia.destraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='sinistra':
      ophelia.sinistraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='avanti':
      ophelia.avantiUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotadx':
      ophelia.ruotaDestraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='stop':
      ophelia.avantiUscita()
      Movement.dataOld='fermo'

def turnRight():
  if Movement.seduto==0:
    if Movement.dataOld=='fermo' or Movement.dataOld=='ruotadx':
      print("ruotadx")
      ophelia.ruotaDestraIngresso()
      ophelia.ruotaDestra()
      Movement.dataOld='ruotadx'
    elif Movement.dataOld=='indietro':
      ophelia.indietroUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='destra':
      ophelia.destraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='sinistra':
      ophelia.sinistraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='avanti':
      ophelia.avantiUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='ruotadx':
      ophelia.ruotaDestraUscita()
      Movement.dataOld='fermo'
    elif Movement.dataOld=='stop':
      ophelia.avantiUscita()
      Movement.dataOld='fermo'

def standup():
  if Movement.dataOld=='fermo' and Movement.seduto==1:
    print("alzata")
    ophelia.alzata()
    Movement.dataOld='fermo'
    Movement.seduto=0
  elif Movement.dataOld=='indietro':
    ophelia.indietroUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='destra':
    ophelia.destraUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='sinistra':
    ophelia.sinistraUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='ruotasx':
    ophelia.ruotaSinistraUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='ruotadx':
    ophelia.ruotaDestraUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='stop':
    ophelia.avantiUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='avanti':
    ophelia.avantiUscita()
    Movement.dataOld='fermo'
  

def sitdown():
  if Movement.dataOld=='fermo' and Movement.seduto==0:
    print("seduta")
    ophelia.seduta()
    Movement.dataOld='fermo'
    Movement.seduto=1
  elif Movement.dataOld=='indietro':
    ophelia.indietroUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='destra':
    ophelia.destraUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='sinistra':
    ophelia.sinistraUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='ruotasx':
    ophelia.ruotaSinistraUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='ruotadx':
    ophelia.ruotaDestraUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='stop':
    ophelia.avantiUscita()
    Movement.dataOld='fermo'
  elif Movement.dataOld=='avanti':
    ophelia.avantiUscita()
    Movement.dataOld='fermo'

bd = BlueDot(cols=5, rows=3)
bd.color = "red"
bd.square = True

bd[0,1].visible = False
bd[1,2].visible = False
bd[1,0].visible = False
bd[2,1].visible = False
bd[3,0].visible = False
bd[3,2].visible = False
bd[4,1].visible = False

bd[2,0].when_pressed = up
bd[2,2].when_pressed = down
bd[1,1].when_pressed = left
bd[3,1].when_pressed = right
bd[0,0].when_pressed = turnLeft
bd[4,0].when_pressed = turnRight
bd[0,2].when_pressed = sitdown
bd[4,2].when_pressed = standup

pause()

    
#!/usr/bin/env python
import rospy
from enum import Enum
from movements import Move
from std_msgs.msg import String
from pynput import keyboard


pub = rospy.Publisher('chatter', Enum, queue_size=1)

rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(50)


def talker(msg):
    pub.publish(msg)
    rate.sleep()


def on_press(key):
    try:
        if format(key.char) == "w":
            rospy.loginfo("avanti")
            talker(Move.FOREWORD)
        elif format(key.char) == "s":
            print("indietro")
            talker(Move.BACKWORD)
        elif format(key.char) == "a":
            print("ruota sinistra")
            talker(Move.LEFT)
        elif format(key.char) == "d":
            print("ruota destra")
            talker(Move.RIGHT)
        elif format(key.char) == "z":
            print("stop")
            talker(Move.STOP)

    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    if key == keyboard.Key.esc:
        return False


while not rospy.is_shutdown():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listen:
        listen.join()

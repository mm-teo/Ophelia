#!/usr/bin/env python

import rospy
from movements import Command
from std_msgs.msg import String
from pynput import keyboard


pub = rospy.Publisher('keyboard_command', String, queue_size=1)

rospy.init_node('keyboard_talker', anonymous=True)
rate = rospy.Rate(50)


def talker(msg):
    pub.publish(msg)
    rate.sleep()


def on_press(key):
    try:
        if format(key.char) == "w":
            rospy.loginfo("Foreward")
            talker(Command.FOREWARD.value)
        elif format(key.char) == "s":
            print("Backward")
            talker(Command.BACKWARD.value)
        elif format(key.char) == "a":
            print("Left rotation")
            talker(Command.LEFT.value)
        elif format(key.char) == "d":
            print("Right rotation")
            talker(Command.RIGHT.value)
        elif format(key.char) == "z":
            print("Stop")
            talker(Command.STOP.value)
        elif format(key.char) == "m":
            print("Changing mode")
            talker(Command.SWITCH_MODE.value)

    except AttributeError:
        print('Special key {0} pressed'.format(key))


def on_release(key):
    if key == keyboard.Key.esc:
        return False


while not rospy.is_shutdown():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listen:
        listen.join()

#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from pynput import keyboard


pub = rospy.Publisher('chatter', String, queue_size=1)

rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(50)


def talker(msg):
    pub.publish(msg)
    rate.sleep()


def on_press(key):
    try:
        if format(key.char) == "w":
            rospy.loginfo("avanti")
            talker(format(key.char))
        elif format(key.char) == "s":
            print("indietro")
            talker(format(key.char))

        elif format(key.char) == "a":
            print("ruota sinistra")
            talker(format(key.char))
        elif format(key.char) == "d":
            print("ruota destra")
            talker(format(key.char))

        elif format(key.char) == "c":
            print("alza")
            talker(format(key.char))
        elif format(key.char) == "x":
            print("abbassa")
            talker(format(key.char))

        elif format(key.char) == "z":
            print("stop")
            talker(format(key.char))

    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    if key == keyboard.Key.esc:
        return False


while not rospy.is_shutdown():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listen:
        listen.join()

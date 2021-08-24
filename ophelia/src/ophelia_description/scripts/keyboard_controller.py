#!/usr/bin/env python

import rospy
from movements import Command
from std_msgs.msg import String
from pynput import keyboard


rospy.init_node(name='keyboard_talker')
pub = rospy.Publisher(name='/keyboard_command',
                      data_class=String,
                      queue_size=1)


def talker(msg):
    pub.publish(msg)


def on_press(key):
    try:
        if format(key.char) == 'w':
            rospy.loginfo('Foreward')
            talker(Command.FOREWARD.value)
        elif format(key.char) == 's':
            rospy.loginfo('Backward')
            talker(Command.BACKWARD.value)
        elif format(key.char) == 'a':
            rospy.loginfo('Left rotation')
            talker(Command.LEFT.value)
        elif format(key.char) == 'd':
            rospy.loginfo('Right rotation')
            talker(Command.RIGHT.value)
        elif format(key.char) == 'z':
            rospy.loginfo('Stop')
            talker(Command.STOP.value)
        elif format(key.char) == 'm':
            rospy.loginfo('Changing mode')
            talker(Command.SWITCH_MODE.value)

    except AttributeError:
        rospy.loginfo('Special key {0} pressed'.format(key))


def on_release(key):
    if key == keyboard.Key.esc:
        return False


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

rospy.spin()

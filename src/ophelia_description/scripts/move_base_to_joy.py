#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy


def convert(val):
    x = val.linear.x
    z = val.angular.z
    z = max(-1, z) if z < 0 else min(1, z)

    output = Joy()
    output.frame_id = "/dev/input/js0"
    output.axes = [0, x, 0, z, 0, 0, 0, 0]
    joy.publish(output)


rospy.init_node(name='move_base_to_joy')
rospy.Rate(10)

joy = rospy.Publisher(name='/joy',
                      data_class=Joy,
                      queue_size=1)

rospy.Subscriber(name='/cmd_vel',
                 data_class=Twist,
                 callback=convert,
                 queue_size=1)

rospy.spin()

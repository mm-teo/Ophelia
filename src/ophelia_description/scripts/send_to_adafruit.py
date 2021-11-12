#!/usr/bin/env python3

from math import degrees
import rospy
from syropod_highlevel_controller.msg import LegState
from adafruit_servokit import ServoKit


class Servos:
    __slots = 'left', 'right'

    def __init__(self):
        self.right = ServoKit(channels=16, address=0x40)
        self.left = ServoKit(channels=16, address=0x41)

    def set_left_arm(self, indexes, values):
        self.left.servo[indexes[0]].angle = values[0]
        self.left.servo[indexes[1]].angle = values[1]
        self.left.servo[indexes[2]].angle = values[2]

    def set_right_arm(self, indexes, values):
        self.right.servo[indexes[0]].angle = values[0]
        self.right.servo[indexes[1]].angle = values[1]
        self.right.servo[indexes[2]].angle = values[2]

    def set_joints(self, arm_state, arm_name):
        arm_state = [degrees(val) for val in arm_state.joint_positions]

        if arm_name[1] == 'L':
            if arm_name[0] == 'A':
                self.set_left_arm(indexes=[13, 14, 15], values=arm_state)
            elif arm_name[0] == 'B':
                self.set_left_arm(indexes=[5, 6, 7], values=arm_state)
            elif arm_name[0] == 'C':
                self.set_left_arm(indexes=[2, 1, 0], values=arm_state)
        elif arm_name[1] == 'R':
            if arm_name[0] == 'A':
                self.set_right_arm(indexes=[13, 14, 15], values=arm_state)
            elif arm_name[0] == 'B':
                self.set_right_arm(indexes=[5, 6, 7], values=arm_state)
            elif arm_name[0] == 'C':
                self.set_right_arm(indexes=[2, 1, 0], values=arm_state)


def main():
    rospy.init_node(name='send_to_adafruit')
    rate = rospy.Rate(10)
    servos = Servos()

    rospy.Subscriber(name='/shc/AL/state',
                     data_class=LegState,
                     callback=servos.set_joints,
                     callback_args='AL',
                     queue_size=1)

    rospy.Subscriber(name='/shc/AR/state',
                     data_class=LegState,
                     callback=servos.set_joints,
                     callback_args='AR',
                     queue_size=1)

    rospy.Subscriber(name='/shc/BL/state',
                     data_class=LegState,
                     callback=servos.set_joints,
                     callback_args='BL',
                     queue_size=1)

    rospy.Subscriber(name='/shc/BR/state',
                     data_class=LegState,
                     callback=servos.set_joints,
                     callback_args='BR',
                     queue_size=1)

    rospy.Subscriber(name='/shc/CL/state',
                     data_class=LegState,
                     callback=servos.set_joints,
                     callback_args='CL',
                     queue_size=1)

    rospy.Subscriber(name='/shc/CR/state',
                     data_class=LegState,
                     callback=servos.set_joints,
                     callback_args='CR',
                     queue_size=1)

    rospy.spin()


if __name__ == '__main__':
    main()

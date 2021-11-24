#!/usr/bin/env python3

import sys
import yaml
import rospy
from adafruit_servokit import ServoKit
from ophelia_description.msg import LegPos


right = ServoKit(channels=16, address=0x40)
left = ServoKit(channels=16, address=0x41)
offsets = None


def set_left_arm(indexes, values):
    left.servo[indexes[0]].angle = values[0]
    left.servo[indexes[1]].angle = values[1]
    left.servo[indexes[2]].angle = values[2]


def set_right_arm(indexes, values):
    right.servo[indexes[0]].angle = values[0]
    right.servo[indexes[1]].angle = values[1]
    right.servo[indexes[2]].angle = values[2]


def set_joints(msg):
    leg_name = msg.legName
    if leg_name[1] == 'L':
        leg_state = [msg.coxa, msg.femur, -msg.tibia]
        if leg_name[0] == 'A':
            indexes = [13, 14, 15]
        elif leg_name[0] == 'B':
            indexes = [5, 6, 7]
        elif leg_name[0] == 'C':
            indexes = [2, 1, 0]

        leg_state = [x + y for x, y in zip(leg_state, offsets[leg_name])]
        set_left_arm(indexes=indexes, values=leg_state)
   elif leg_name[1] == 'R':
        leg_state = [msg.coxa, -msg.femur, msg.tibia]
        if leg_name[0] == 'A':
            indexes = [2, 1, 0]
        elif leg_name[0] == 'B':
            indexes = [5, 6, 7]
        elif leg_name[0] == 'C':
            indexes = [13, 14, 15]

        leg_state = [x + y for x, y in zip(leg_state, offsets[leg_name])]
        set_right_arm(indexes=indexes, values=leg_state)


def main():
    global offsets
    rospy.init_node(name='send_to_adafruit')
    with open(sys.argv[1], 'r') as f:
        try:
            offsets = yaml.safe_load(f)
        except yaml.YAMLError:
            rospy.logerr('Error parsing')
            sys.exit(1)

    rate = rospy.Rate(20)

    rospy.Subscriber(name='/raspi_command',
                     data_class=LegPos,
                     callback=set_joints,
                     queue_size=5)

    rospy.spin()


if __name__ == '__main__':
    main()

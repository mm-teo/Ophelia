#!/usr/bin/env python2

from math import degrees
import rospy
from ophelia_description.msg import LegPos
from syropod_highlevel_controller.msg import LegState


class Servos:
    __slots__ = 'pub'

    def __init__(self, rospy):
        self.pub = rospy.Publisher(name='raspi_command',
                                   data_class=LegPos,
                                   queue_size=10)

    def set_joints(self, arm_state, arm_name):
        arm_state = [degrees(val) for val in arm_state.joint_positions]

        msg = LegPos()
        msg.legName = arm_name
        msg.coxa = arm_state[0]
        msg.femur = arm_state[1]
        msg.tibia = arm_state[2]
        self.pub.publish(msg)


def main():
    rospy.init_node(name='send_to_raspi')
    rate = rospy.Rate(25)
    servos = Servos(rospy)

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

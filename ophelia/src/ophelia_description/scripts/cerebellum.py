#!/usr/bin/env python

import threading
import time

import rospy
from std_msgs.msg import String, Bool
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from rtabmap_ros.msg import OdomInfo

from movements import Command

state = None
discrete_mov = None


class CerebellumState:
    __slots__ = 'auto_move', 'obstacled', 'goal_reached', \
                'next_pose', 'current_pose', 'odom_quality'

    def __init__(self,
                 auto_move=False,
                 obstacled=True,
                 goal_reached=False,
                 odom_quality=0):
        self.auto_move = auto_move
        self.obstacled = obstacled
        self.goal_reached = goal_reached
        self.odom_quality = odom_quality
        th = threading.Thread(target=self.cycle)
        th.daemon = True
        th.start()

    def set_keyboard_command(self, command):
        command = Command(command.data)
        if command == Command.SWITCH_MODE:
            self.auto_move = not self.auto_move
            self.goal_reached = False
        elif not self.auto_move:
            if not self.obstacled:
                discrete_mov.publish(command.value)

    def set_obstacle(self, obstacled):
        self.obstacled = obstacled

    def set_goal_reached(self, goal_reached):
        self.goal_reached = goal_reached

    def set_next_pose(self, next_pose):
        self.next_pose = next_pose

    def set_current_pose(self, odom):
        self.current_pose = odom.pose.pose

    def set_odom_quality(self, odom_info):
        self.odom_quality = odom_info.inliers

    def cycle(self):
        while True:
            time.sleep(0.5)
            if self.auto_move and not self.obstacled and not self.goal_reached:
                self.update_direction()
            elif self.goal_reached:
                self.set_next_pose(None)
                self.set_goal_reached(False)

    def update_direction(self):
        pass


def main():
    global state, discrete_mov

    rospy.init_node(name='cerebellum')

    state = CerebellumState()

    rospy.Subscriber(name='/rtabmap/odom',
                     data_class=Odometry,
                     callback=state.set_current_pose,
                     queue_size=1)

    rospy.Subscriber(name='/rtabmap/odom_info_lite',
                     data_class=OdomInfo,
                     callback=state.set_odom_quality,
                     queue_size=1)

    rospy.Subscriber(name='/rtabmap/goal_out',
                     data_class=PoseStamped,
                     callback=state.set_next_pose,
                     queue_size=1)

    rospy.Subscriber(name='/rtabmap/goal_reached',
                     data_class=Bool,
                     callback=state.set_goal_reached,
                     queue_size=1)

    rospy.Subscriber(name='/exist_obstacle',
                     data_class=Bool,
                     callback=state.set_obstacle,
                     queue_size=1)

    rospy.Subscriber(name='/keyboard_command',
                     data_class=String,
                     callback=state.set_keyboard_command,
                     queue_size=1)

    discrete_mov = rospy.Publisher(name='/discrete_movement',
                                   data_class=String,
                                   queue_size=1)

    rospy.spin()


if __name__ == '__main__':
    main()

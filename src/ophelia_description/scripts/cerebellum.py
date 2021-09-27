#!/usr/bin/env python

import threading
from math import pi

import rospy
from std_msgs.msg import String, Bool
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from rtabmap_ros.msg import OdomInfo
from tf.transformations import euler_from_quaternion as to_euler

from movements import Command

discrete_mov = None


class CerebellumState:
    __slots__ = 'rate', 'auto_move', 'obstacled', 'goal_reached', \
                'next_pose', 'current_pose', 'odom_quality'

    def __init__(self,
                 rate,
                 auto_move=False,
                 obstacled=True,
                 goal_reached=False,
                 odom_quality=0):
        self.rate = rate
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
            else:
                rospy.loginfo('Obstacle: no way to proceed')

    def set_obstacle(self, obstacled):
        self.obstacled = obstacled.data

    def set_goal_reached(self, goal_reached):
        self.goal_reached = goal_reached

    def set_next_pose(self, next_pose):
        self.next_pose = next_pose.pose

    def set_current_pose(self, odom):
        self.current_pose = odom.pose.pose

    def set_odom_quality(self, odom_info):
        self.odom_quality = odom_info.inliers

    def cycle(self):
        while True:
            if self.odom_quality <= 150:
                rospy.logerr('!!!!!Totally losing odometry. Go slower!!!!!')
            elif self.odom_quality <= 250:
                rospy.logwarn('Low odometry. Go slower!')
            if self.auto_move and not self.obstacled and not self.goal_reached:
                if self.odom_quality > 250:
                    self.update_direction()
            elif self.goal_reached:
                rospy.loginfo('!!!Arrived!!!')
                self.set_next_pose(None)
                self.set_goal_reached(False)
            # elif self.obstacled:
            #     rospy.loginfo('Obstacle: no way to proceed')

            self.rate.sleep()

    def update_direction(self):
        next_yaw = to_euler([self.next_pose.orientation.x,
                             self.next_pose.orientation.y,
                             self.next_pose.orientation.z,
                             self.next_pose.orientation.w])[2]
        current_yaw = to_euler([self.current_pose.orientation.x,
                                self.current_pose.orientation.y,
                                self.current_pose.orientation.z,
                                self.current_pose.orientation.w])[2]

        print("*************************** ",next_yaw - current_yaw)
        print("*************************** ",self.next_pose.position.x)
        print("*************************** ",self.current_pose.position.x)
        print("*************************** ",self.next_pose.position.y - self.current_pose.position.y)
        print("*************************** ",self.next_pose.position.z - self.current_pose.position.z)


        if next_yaw - current_yaw > pi/6:
            rospy.loginfo('Right rotation')
            discrete_mov.publish(Command.RIGHT.value)
        elif next_yaw - current_yaw < -pi/6:
            rospy.loginfo('Left rotation')
            discrete_mov.publish(Command.LEFT.value)
        elif self.next_pose.position.x - self.current_pose.position.x > 1:
            rospy.loginfo('Foreward')
            discrete_mov.publish(Command.FOREWARD.value)
        else:
            rospy.loginfo('Stop')
            discrete_mov.publish(Command.STOP.value)


def main():
    global discrete_mov

    rospy.init_node(name='cerebellum')
    rate = rospy.Rate(10)

    state = CerebellumState(rate=rate)

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

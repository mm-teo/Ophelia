import threading
import time

import rospy
from std_msgs.msg import String

from movements import Command

state = None
discrete_mov = None


class CerebellumState:
    __slots__ = 'auto_move'

    def __init__(self,
                 auto_move=False):
        self.auto_move = auto_move
        th = threading.Thread(target=self.cycle)
        th.daemon = True
        th.start()

    def set_keyboard_command(self, command):
        command = Command(command.data)
        if command == Command.SWITCH_MODE:
            self.auto_move = not self.auto_move
        elif not self.auto_move:
            discrete_mov.publish(command.value)

    def cycle(self):
        while True:
            time.sleep(1)
            if self.auto_move:
                self.update_direction()

    def update_direction(self):
        pass


def main():
    global state, discrete_mov

    rospy.init_node(name='cerebellum')

    state = CerebellumState()

    """rospy.Subscriber(name='/rtabmap/odom',
                     data_class=Image,
                     callback=convert_depth_image,
                     queue_size=1)

    rospy.Subscriber(name='/rtabmap/goal_out',
                     data_class=Image,
                     callback=convert_depth_image,
                     queue_size=1)

    rospy.Subscriber(name='/rtabmap/goal_reached',
                     data_class=Image,
                     callback=convert_depth_image,
                     queue_size=1)

    rospy.Subscriber(name='/exist_obstacle',
                     data_class=Image,
                     callback=convert_depth_image,
                     queue_size=1)
"""
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

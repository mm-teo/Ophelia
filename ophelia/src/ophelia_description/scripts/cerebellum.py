import threading
import time

import rospy
from std_msgs.msg import String

from movements import Command

state = None
discrete_mov = None


class CerebellumState:
    __slots__ = 'auto_move', 'keyboard_command'

    def __init__(self,
                 auto_move=False,
                 keyboard_command=Command('')):
        self.auto_move = auto_move
        self.keyboard_command = keyboard_command
        th = threading.Thread(target=self.cycle)
        th.daemon = True
        th.start()

    def set_keyboard_command(self, command):
        command = Command(command.data)
        if command == Command.SWITCH_MODE:
            self.auto_move = not self.auto_move
        else:
            self.keyboard_command = command
            self.update_direction()

    def cycle(self):
        while True:
            time.sleep(1)
            if self.auto_move:
                self.update_direction()

    def update_direction(self):
        if self.auto_move:
            pass
        else:
            discrete_mov.publish(self.keyboard_command.value)


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

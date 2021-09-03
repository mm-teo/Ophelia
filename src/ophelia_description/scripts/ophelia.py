#! /usr/bin/env python

import rospy
from std_msgs.msg import String

from movements import Command
import hexamove as hxmove


class Movement:
    __slots__ = 'old_cmd'

    def __init__(self):
        self.old_cmd = Command.DEFAULT

    def alza(self):
        hxmove.alza()

    def avanti(self):
        hxmove.avanti()

    def avantiUscita(self):
        hxmove.avanti_uscita()

    def indietro(self):
        hxmove.indietro()

    def indietroUscita(self):
        hxmove.indietro_uscita()

    def ruotaDestra(self):
        hxmove.ruota_destra()

    def ruotaDestraUscita(self):
        hxmove.ruota_destra_uscita()

    def ruotaSinistra(self):
        hxmove.ruota_sinistra()

    def ruotaSinistraUscita(self):
        hxmove.ruota_sinistra_uscita()

    def to_default_position(self):
        if self.old_cmd == Command.BACKWARD:
            self.indietroUscita()
        elif self.old_cmd == Command.FOREWARD:
            self.avantiUscita()
        elif self.old_cmd == Command.LEFT:
            self.ruotaSinistraUscita()
        elif self.old_cmd == Command.RIGHT:
            self.ruotaDestraUscita()
        self.old_cmd = Command.DEFAULT

    def control_movement(self, command, move):
        if self.old_cmd == command or self.old_cmd == Command.DEFAULT:
            move()
            self.old_cmd = command
        else:
            self.to_default_position()


def process_command(movement):
    command = Command(movement.data)
    if command == Command.FOREWARD:
        robot.control_movement(command, robot.avanti)
    elif command == Command.BACKWARD:
        robot.control_movement(command, robot.indietro)
    elif command == Command.LEFT:
        robot.control_movement(command, robot.ruotaSinistra)
    elif command == Command.RIGHT:
        robot.control_movement(command, robot.ruotaDestra)
    elif command == Command.STOP:
        if robot.old_cmd == command or robot.old_cmd == Command.DEFAULT:
            robot.old_cmd = Command.DEFAULT
        else:
            robot.to_default_position()


if __name__ == '__main__':
    hxmove.init_publisher()
    rospy.init_node('joint_state_interface')

    robot = Movement()
    robot.alza()

    rospy.Subscriber(name='/discrete_movement',
                     data_class=String,
                     callback=process_command,
                     queue_size=1)

    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        print('Stopping ophelia')
    hxmove.shutdown_publisher()

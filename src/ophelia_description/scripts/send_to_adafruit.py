import rospy
from adafruit_servokit import ServoKit
from random.msg import LegPos


right = ServoKit(channels=16, address=0x40)
left = ServoKit(channels=16, address=0x41)


def set_left_arm(self, indexes, values):
    left.servo[indexes[0]].angle = values[0]
    left.servo[indexes[1]].angle = values[1]
    left.servo[indexes[2]].angle = values[2]


def set_right_arm(self, indexes, values):
    right.servo[indexes[0]].angle = values[0]
    right.servo[indexes[1]].angle = values[1]
    right.servo[indexes[2]].angle = values[2]


def set_joints(msg):
    leg_name = msg.legName
    leg_state = [msg.coxa, msg.femur, msg.tibia]
    if leg_name[1] == 'L':
        if leg_name[0] == 'A':
            set_left_arm(indexes=[13, 14, 15], values=leg_state)
        elif leg_name[0] == 'B':
            set_left_arm(indexes=[5, 6, 7], values=leg_state)
        elif leg_name[0] == 'C':
            set_left_arm(indexes=[2, 1, 0], values=leg_state)
    elif leg_name[1] == 'R':
        if leg_name[0] == 'A':
            set_right_arm(indexes=[13, 14, 15], values=leg_state)
        elif leg_name[0] == 'B':
            set_right_arm(indexes=[5, 6, 7], values=leg_state)
        elif leg_name[0] == 'C':
            set_right_arm(indexes=[2, 1, 0], values=leg_state)


def main():
    rospy.init_node(name='send_to_adafruit')
    rate = rospy.Rate(20)
    servos = Servos(rospy)

    rospy.Subscriber(name='/raspi_command',
                     data_class=LegPos,
                     callback=set_joints,
                     queue_size=10)

    rospy.spin()


if __name__ == '__main__':
    main()

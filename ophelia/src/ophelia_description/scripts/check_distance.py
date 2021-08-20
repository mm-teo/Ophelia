#!/usr/bin/env python
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
import numpy as np
import argparse

publish_obs = rospy.Publisher(name='exist_obstacle',
                              data_class=Bool,
                              queue_size=1)


def convert_depth_image(image, kwargs):
    bridge = CvBridge()

    try:
        depth_image = bridge.imgmsg_to_cv2(img_msg=image,
                                           desired_encoding='passthrough')
        depth_array = np.array(depth_image, dtype=np.float32)

        depth_array = depth_array[0:int(depth_array.shape[0]/4*3), :]
        depth_array = depth_array[::5, ::5]
        nearest = (depth_array < kwargs['distance_threshold']).sum()

        publish_obs.publish(nearest > (depth_array.size)*kwargs['stop_ratio'])
    except CvBridgeError:
        print('Error interpreting depth value')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--distance-threshold', type=int)
    parser.add_argument('--stop-ratio', type=float)
    args, unknown = parser.parse_known_args()
    args = vars(args)
    if args['distance_threshold'] <= 200:
        print('Error: distance-threshold must be greater than 200')
        exit(1)
    if not(0 < args['stop_ratio'] < 1):
        print('Error: stop-ratio must be a ratio')
        exit(1)

    rospy.init_node(name='distance_checker')
    rospy.Subscriber(name='/camera/aligned_depth_to_color/image_raw',
                     data_class=Image,
                     callback=convert_depth_image,
                     callback_args=args,
                     queue_size=5)

    rospy.spin()


if __name__ == '__main__':
    main()

import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
import numpy as np
import argparse

publish_obs = None


def convert_depth_image(image, args):
    bridge = CvBridge()
    try:
        depth_image = bridge.imgmsg_to_cv2(img_msg=image,
                                           desired_encoding='passthrough')
        depth_array = np.array(depth_image, dtype=np.float32)

        depth_array = depth_array[0:int(depth_array.shape[0]/4*3), :]
        depth_array = depth_array[::5, ::5]
        nearest = (depth_array < args['distance_threshold']).sum()

        publish_obs.publish(nearest > (depth_array.size)*args['stop_ratio'])
    except CvBridgeError:
        print('Error interpreting depth value')


def main():
    global publish_obs

    parser = argparse.ArgumentParser()
    parser.add_argument('--distance-threshold', type=int)
    parser.add_argument('--stop-ratio', type=float)
    args = vars(parser.parse_args())
    if args['distance_threshold'] <= 200:
        print('Error: distance-threshold must be greater than 200')
        exit(1)
    if not(0 < args['stop_ratio'] < 1):
        print('Error: stop-ratio must be a ratio')
        exit(1)

    rospy.init_node(name='distance_checker')
    rospy.Subscriber('/camera/aligned_depth_to_color/image_raw',
                     Image,
                     convert_depth_image, args,
                     5)
    publish_obs = rospy.Publisher(name='exist_obstacle',
                                  data_class=Bool,
                                  queue_size=1)

    rospy.spin()


if __name__ == '__main__':
    main()
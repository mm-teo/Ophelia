import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
import numpy as np

publish_obs = None


def convert_depth_image(ros_image):
    bridge = CvBridge()

    try:
        depth_image = bridge.imgmsg_to_cv2(img_msg=ros_image,
                                           desired_encoding='passthrough')
        depth_array = np.array(depth_image, dtype=np.float32)

        depth_array = depth_array[0:int(depth_array.shape[0]/4*3), :]
        depth_array = depth_array[::5, ::5]
        nearest = (depth_array < 250).sum()

        publish_obs.publish(True if nearest > (depth_array.size)/4 else False)
    except CvBridgeError:
        print('Error interpreting depth value')


def main():
    global publish_obs
    rospy.init_node(name='distance_checker')

    rospy.Subscriber(name='/camera/aligned_depth_to_color/image_raw',
                     data_class=Image,
                     callback=convert_depth_image,
                     queue_size=5)
    publish_obs = rospy.Publisher(name='exist_obstacle',
                                  data_class=Bool,
                                  queue_size=1)

    rospy.spin()


if __name__ == '__main__':
    main()

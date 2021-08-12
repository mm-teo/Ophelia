# Software requirements

Operating System: Ubutnu 18.04\
ROS: Melodic

# Hardware requirements

Real Sense D435\
kinect xbox 360

# First approach

[rrt_exploration](http://wiki.ros.org/rrt_exploration)\
[gmapping](http://wiki.ros.org/gmapping)\
*This approach was never used since we wanted to use real sensor over the robot*

# Second approach

[rtabmap_ros](http://wiki.ros.org/rtabmap_ros/Tutorials/HandHeldMapping)

This library allows us to use some cheaper sensor for the sapce anlysis, the one we used were:
- Real Sense D435
- Kinect xbox 360

For the set-up of the devices and the library we used:
- [RealSense](http://wiki.ros.org/RealSense)
- [librealsense2](http://wiki.ros.org/librealsense2)

Then we tested the base mapping following the guide mapping using:
```
$ roslaunch rtabmap_ros rtabmap.launch \
   rtabmap_args:="--delete_db_on_start" \
   depth_topic:=/camera/aligned_depth_to_color/image_raw \
   rgb_topic:=/camera/color/image_raw \
   camera_info_topic:=/camera/color/camera_info \
   approx_sync:=false
```
The result of the library is the 3D and 2D map of the envoirment, this map can then be used to perform the localization of the camera, so the camera knows where it is in the previus analyzed sapce. The map is found at:

```
~/.ros/rtabmap.db
```
For Showing the map use:
```
rtabmap-databaseViewer ~/.ros/rtabmap.db
```
**NOTE: The camera using this packet works**

# TODO list

1. Mappare la zona a mano con i comandi base del robot
  1. Mappare facendolo andare dritto e poi ruotare se siamo troppo vicini al muro
1. Una volta mappata la zona utilizzare il grafo generato dal pacchetto per poi consentire al robot di spostarsi da un punto ad un'altro

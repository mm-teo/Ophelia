# Software requirements

Operating System: Ubutnu 18.04\
ROS: Melodic

# Hardware requirements

Real Sense D435: *Tested* \
kinect xbox One: *Tested* (but too heavy)\
kinect xbox 360: *Not Tested*

# First approach

[rrt_exploration](http://wiki.ros.org/rrt_exploration)\
[gmapping](http://wiki.ros.org/gmapping)\
*This approach was never used since we wanted to use real sensor over the robot*

# Second approach

[rtabmap_ros](http://wiki.ros.org/rtabmap_ros/Tutorials/HandHeldMapping)

This library allows us to use some cheaper sensor for the sapce anlysis, the one we used were:
- Real Sense D435
- Kinect xbox One
- Kinect xbox 360

For the set-up of the devices and the library we used:
- [RealSense](http://wiki.ros.org/RealSense)
- [librealsense2](http://wiki.ros.org/librealsense2)
- [octomap-rviz-plugins](http://wiki.ros.org/octomap_rviz_plugins)

Then we tested the base mapping following the guide mapping using:
```
roslaunch rtabmap_ros rtabmap.launch \
   rtabmap_args:="--delete_db_on_start" \
   depth_topic:=/camera/aligned_depth_to_color/image_raw \
   rgb_topic:=/camera/color/image_raw \
   camera_info_topic:=/camera/color/camera_info \
   approx_sync:=false
```
or use:
```
roslaunch realsense2_camera rs_camera.launch align_depth:=true
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

# Report

* **NOTE: used python2 and not python3 because cv_bridge must be recompiled to python3 in order to be executed, for testing reason and time we used python2 for that, if possible we will recompile it.**
* We defined a script that read the raw data from the sensor and measure the distance from it, this will allow us to know if some new obstacle *Not present in the mapped area* is now present. This boolean function keep sendig data to the topic:
```
/camera/exist_obstacle
```

**Filtering image raw:**
* start from 640x480.
* cancellati le righe piu basse dell'immagine in quanto il robot è basso e potrebbe pensare che il terreno sia un ostacolo.
* campiono ogni 5 pixel: 128x96
* contiamo solo i pixel con valore parametrico (>200), se questi sono più di una certa ratio parametrica, allora c'è un ostacolo.
altrimenti non vi è un ostacolo.
* We fix and generate the specific comand to be able to move the robot

# TODO list

1. :heavy_check_mark: Mappare e salvare la nuova area
2. :heavy_check_mark: Spostare il robot a mano stopparlo nel caso sia troppo vicino ad un ostacolo
3. Alternative:
   1. :x: Una volta mappata la zona utilizzare il grafo generato dal pacchetto per poi consentire al robot di spostarsi da un punto ad un'altro
   2. :x: Da rviz segnare un goal; esso verrà pubblicato nel topic "/move_base_simple/goal"; ripubblicarlo in "/rtabmap/goal" o altro; vedere se viene generato il path.  

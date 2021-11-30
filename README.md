# Ophelia
This project is about a 18DOF Hexapode driven by Raspberry 4 Model B 4GB RAM, 18 MG996r high torque servomotors.

Remember to use python2 (pip2) if not the default of the system.

## Dependencies

Install with pip the package:

`pip install pynput pybind11`

# Build
`catkin_make`

# Run
Before starting the program (e.g. with bash):

`source devel/setup.bash`

Start the program:

`roslaunch ophelia_description display.launch`


## Dependencies
Install with pip the package:

`pip install pynput pybind11`

Install on the os the following package:

- `sudo apt install ros-melodic-joy` [Git](https://github.com/ros-drivers/joystick_drivers)
- [librealsense2](http://wiki.ros.org/librealsense2)

# How to install
* Install the Dependencies
* Download the repo and the dependencies
``` bash
git clone --recurse-submodules git@github.com:Tambup/Ophelia.git
```
* Build the packet
``` bash
cd Ophelia
catkin_make
```
* Before starting the program (e.g. with bash)
 ``` bash
 source devel/setup.bash
 ```
* Start the program
``` bash
roslaunch ophelia_description display.launch
```

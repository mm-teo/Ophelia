# Ophelia
This project is about a 18DOF Hexapode driven by Raspberry 4 Model B 4GB RAM, 18 MG996r high torque servomotors. I decided to adopt a ROS environment because in the future it could become a bigger project without painfull or impossible modify.

# Build
```
cd ophelia
catkin_make
```

## Dependencies

Install with pip the package:

`pip install pynput`

# Run
Before starting the program (with bash):

`source ophelia/devel/setup.bash`

Start the program:

`roslaunch ophelia_description display.launch`

To control the robot, in another shell inside the repository:

`python ophelia/src/ophelia_description/scripts/ophelia_main2.py`

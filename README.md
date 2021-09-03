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

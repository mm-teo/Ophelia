# Setup
Nesessario per fare partire il comando roslaunch

`source devel/setup.bash`

## Necessario per la prima esecuzione

`cd Ophelia/ophelia/src/ophelia_description/launch`

`vim display.launch`

update the node with:

`<node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />`

Install with pip the packege

`pip install pynput`

## Da eseguire ogni volta che si utilizza il prgramma

`roslaunch ophelia_description display.launch`

then in another terminal kill the node (Test if is necessary proably yes):
`rosnode kill /joint_state_publisher`

For controlling the robot execute:

`cd Ophelia/ophelia/src/ophelia_description/scripts`

`python ophelia_main2.py`

# Goals

## /rtabmap/odom
Actual position of the robot in the map inside the "pose" attribute.

## /rtabmap/goal_out
Next position to reach.

## /rtabmap/goal_reached
True if the goal is reached.

## /rtabmap/global_path
Initial and final position of the current goal.

## Rerirecting
To redirect from rviz goal to rtabmap goal.

### From CLI
```
rosrun topic_tools relay /move_base_simple/goal /rtabmap/goal
```
### From .launch file
```
<node name="forwardToB" pkg="topic_tools" type="relay" args="/move_base_simple/goal /rtabmap/goal"/>
```

# Obstacle

## /camera/aligned_depth_to_color/image_raw
Read from this topic to receive the distance matrix image.

## /exist_obstacle
Return True if there is a obstacle.

# Movement

## /robot_discrete/movement
Generate output from custom script using /rtabmap/odom, /rtabmap/goal_out, /rtabmap/goal_reached, /exist_obstacle and /chatter.

/chatter and other topics are mutually exclusive.

The output is of form:
 -  left/right
 -  forward/backward

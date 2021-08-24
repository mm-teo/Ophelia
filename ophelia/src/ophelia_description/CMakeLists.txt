################################################################################
# Set minimum required version of cmake, project name and compile options
################################################################################
cmake_minimum_required(VERSION 2.8.3)
project(ophelia_description)

################################################################################
# Find catkin packages and libraries for catkin and system dependencies
################################################################################
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
)

################################################################################
# Declare catkin specific configuration to be passed to dependent projects
################################################################################
catkin_package(
  CATKIN_DEPENDS roscpp std_msgs sensor_msgs
)

################################################################################
# Build
################################################################################
include_directories(${catkin_INCLUDE_DIRS})

add_library(hexamove SHARED
  src/HexaMove.cpp
)

set_target_properties(hexamove PROPERTIES VERSION 1.0.0)
set_target_properties(hexamove PROPERTIES SOVERSION 1)

target_link_libraries(hexamove ${catkin_LIBRARIES})

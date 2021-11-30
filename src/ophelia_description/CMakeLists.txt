################################################################################
# Set minimum required version of cmake, project name and compile options
################################################################################
cmake_minimum_required(VERSION 3.4)
project(ophelia_description)

# specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

################################################################################
# Find catkin packages and libraries for catkin and system dependencies
################################################################################
find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
  message_generation
)

add_message_files(
  FILES
  LegPos.msg
)

################################################################################
# Declare catkin specific configuration to be passed to dependent projects
################################################################################
generate_messages(DEPENDENCIES std_msgs)
catkin_package(
  CATKIN_DEPENDS roscpp std_msgs sensor_msgs message_runtime
)

################################################################################
# Build
################################################################################
include_directories(${catkin_INCLUDE_DIRS})

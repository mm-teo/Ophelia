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
execute_process(
  COMMAND "${PYTHON_EXECUTABLE}" -m pybind11 --cmakedir
  OUTPUT_VARIABLE _tmp_dir
  OUTPUT_STRIP_TRAILING_WHITESPACE)
list(APPEND CMAKE_PREFIX_PATH "${_tmp_dir}")

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
  sensor_msgs
)

find_package(pybind11 CONFIG REQUIRED)

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

set_target_properties(hexamove PROPERTIES VERSION 1.0.1)
set_target_properties(hexamove PROPERTIES SOVERSION 1)

target_link_libraries(hexamove ${catkin_LIBRARIES})
target_link_libraries(hexamove pybind11::module pybind11::lto)

pybind11_extension(hexamove)
pybind11_strip(hexamove)

cmake_minimum_required(VERSION 3.10.2)
project(turtlebot_description)

find_package(ament_cmake QUIET)

# used later when it does not work: tell Gazebo to look for files here
#ament_environment_hooks("hooks/resource_paths.dsv.in")

install(DIRECTORY urdf meshes DESTINATION share/${PROJECT_NAME})

ament_package()

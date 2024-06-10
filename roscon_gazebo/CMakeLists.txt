cmake_minimum_required(VERSION 3.10.2)
project(roscon_gazebo)

find_package(ament_cmake QUIET)

#ament_environment_hooks("hooks/resource_paths.dsv.in")

install(DIRECTORY urdf launch DESTINATION share/${PROJECT_NAME})

ament_package()

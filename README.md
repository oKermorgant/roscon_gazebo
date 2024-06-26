# Gazebo tutorial @ ROSCon FR 2024

This repo consists in two packages to learn about how to interface ROS 2 and Gazebo (the new one).

## Dependencies:

- `simple_launch`
- `slider_publisher`
- [`pose_to_tf`](https://github.com/oKermorgant/pose_to_tf) for the Turtlebot part

## Available packages

- `roscon_gazebo` to run a basic world with a turret robot
- `turtlebot_description` emulates a classical description package with meshes, in order to highlight the use of environment hooks to allow Gazebo resolve `package://` URI.

## Initial state

Most of the things will not work initially. Functional parts of the files (URDF / launch) are simply commented out in order to highlight the mechanics of ROS and Gazebo integration.



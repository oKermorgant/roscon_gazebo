from simple_launch import SimpleLauncher, GazeboBridge

sl = SimpleLauncher(use_sim_time=True)
sl.declare_arg('mode', 'velocity')


def launch_setup():

    mode = sl.arg('mode')

    # run the simulation
    sl.gz_launch(sl.find('roscon_gazebo', 'world.sdf'), '-r')

    ns = 'turret'

    with sl.group(ns = ns):

        sl.robot_state_publisher('roscon_gazebo', 'turret.xacro',
                                 xacro_args = sl.arg_map('mode'))

        sl.spawn_gz_model(ns)

        # manual control
        sl.node('slider_publisher',
                arguments = [sl.find('roscon_gazebo', mode + '_manual.yaml')])

        # build bridges
        bridges = [GazeboBridge.clock()]

        # cmd_vel for joints with explicit GazeboBridge
        for joint in ('joint1', 'joint2', 'joint3'):

            if mode == 'velocity':
                bridges.append(GazeboBridge(f'{ns}/{joint}_cmd_vel', f'{joint}_cmd_vel',
                                        'std_msgs/Float64', GazeboBridge.ros2gz))
            else:
                bridges.append(GazeboBridge(f'/model/turret/joint/{joint}/0/cmd_pos',
                                            f'{joint}_cmd_pos',
                                            'std_msgs/Float64',
                                            GazeboBridge.ros2gz))

        # joint state feedback on /world/<world>/model/<model>/joint_state
        gz_js_topic = GazeboBridge.model_prefix(ns) + '/joint_state'
        bridges.append(GazeboBridge(gz_js_topic, 'joint_states', 'sensor_msgs/JointState', GazeboBridge.gz2ros))

        # image with lazy construction (no GazeboBridge, only tuple with arguments)
        bridges.append((f'{ns}/image', 'image', 'sensor_msgs/Image', GazeboBridge.gz2ros))

        sl.create_gz_bridge(bridges)

    # also display in RViz
    sl.rviz(sl.find('roscon_gazebo', 'layout.rviz'))

    return sl.launch_description()


generate_launch_description = sl.launch_description(launch_setup)

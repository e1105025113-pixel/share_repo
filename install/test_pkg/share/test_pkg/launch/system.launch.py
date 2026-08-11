from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='test_pkg',
            executable='publisher',
            name='publisher',
            output='screen'
        ),

        Node(
            package='test_pkg',
            executable='subscriber',
            name='subscriber',
            output='screen'
        ),
    ])

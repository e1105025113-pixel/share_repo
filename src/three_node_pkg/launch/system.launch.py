from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
		Node(
			package='three_node_pkg',
			executable='input',
			name='input',
			output='screen',
		),
	])

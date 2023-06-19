import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
          
            Node(
                name='beagle_action_client',
                package='beagle_first_package',
                executable='beagle_action_client',
                output='screen'
            ),

            Node(
                name='beagle_first_pub',
                package='beagle_first_package',
                executable='beagle_first_pub',
                output='screen'
            ),
            Node(
                name='beagle_my_pos',
                package='beagle_my_pos',
                executable='beagle_my_pos',
                output='screen'
            )
        ]
    )
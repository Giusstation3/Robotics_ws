#imports launch description, lo que el launch va a ejecutar 
from launch import LaunchDescription
 
from launch_ros.actions import Node

#ros2 busca la funcion con este nombre
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',  
            output='screen' 
        ),
        Node(
            package='basics',
            executable='joystick_pub',
	    output='screen'
        ),
        Node(
            package='basics',
            executable='turtle_controller',
	    output='screen'
        ),
    ])

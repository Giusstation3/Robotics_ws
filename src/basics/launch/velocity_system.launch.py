#imports launch description, lo que el launch va a ejecutar 
from launch import LaunchDescription
#importamos node, accion de un nodo ros2 a lanzar 
from launch_ros.actions import Node

#ros2 busca la funcion con este nombre
def generate_launch_description():

    return LaunchDescription([
        #nodo publicador de la velocidad de /velocity
        Node(
            package='basics', # le decimos en que paquete se encuentra el nodo
            executable='velocity_publisher', #le decimos que es lo que tiene que ejecutar 
            output='screen' #mostramos en la terminal
        ),
        #nodo subscriptor recibe la velocidad de velocity 
        Node(
            package='basics',
            executable='velocity_subscriber',
            output='screen'
        ),

    ])

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

#Definicion de la clase
class VelocitySubscriber(Node):

    def __init__(self):
	#Crea la suscripcion al topico /velocity con una cola de mensajes 10 
        super().__init__('velocity_subscriber')
        self.subscription_ = self.create_subscription(Float32,'/velocity',self.velocity_callback,10)

    def velocity_callback(self, msg):
	#Extraemos el valor del mensaje 
        Velocity = msg.data
	#mensaje en la terminal con la informacion con formato
        self.get_logger().info(f'Vel = {Velocity:.1f} m/s')


def main(args = None):
#incializamos el ROS2, creamos la instancia de velocity, lo mantenemos en bucle con rclpy.spin  y destruimos el nodo y apagamos ROS2
    rclpy.init(args=args)
    node = VelocitySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

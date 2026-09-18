import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32 #Mensaje entero entonces solo mandamos un cero o un uno
 

class LedBlink(Node):
    def __init__(self):
        super().__init__('led_blink') #llamo un nodo led_blink y creamos el publisher con el topico Led_command
        self.publisher_ = self.create_publisher(Int32, '/led_command', 10)

        self.estado = 1 #Guardamos el status del led 
        self.timer_ = self.create_timer(1.0, self.blink_callback)
        self.get_logger().info('Nodo iniciado')
        self.publicar_estado() #se publica luego luego el estado del led 

	#id básico para alternar los estados del led
    def blink_callback(self):
        if self.estado == 1:
            self.estado = 0
        else:
            self.estado = 1

        self.publicar_estado()

	#funcion para publicar el estado del nodo
    def publicar_estado(self):
        msg = Int32()
        msg.data = self.estado

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: {self.estado}')
	#iniciamos comunicacion con ros2, creamos una instancia del nodo ledBlink, spin mantiene el programa en loop, el destroy es para poder interrumpir con control c, y shutdown para cerrar la comunicacion con Ros2
def main(args=None):
    rclpy.init(args=args)
    node = LedBlink()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

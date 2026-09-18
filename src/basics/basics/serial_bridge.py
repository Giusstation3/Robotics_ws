import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial #para que podamos escribir en puertos seriales dev/ttyUSB0 

#El puente entre ros2 y el puerto serial. 
class SerialBridge(Node):
    def __init__(self):
        super().__init__('serial_bridge')
	#Creamos el subscriptor para led_command, cuando recibimos un mensaje de ahí llamamos a la función led call back
        self.subscription_ = self.create_subscription(Int32, '/led_command', self.led_callback,10)
        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1) #seleccionamos el puerto serial que queremos abrir
	
        self.get_logger().info('Esperando mensajes')
	#recibe el mensaje cuando llega algo al topico ledcommand
    def led_callback(self, msg):
        if msg.data == 1:
            self.serial_.write(b'1\n') #dependiendo de si es 1 o 0 manda un mensaje diferente al puerto seraial 
            self.get_logger().info('ROS 2 -> Serial: 1')

        elif msg.data == 0:
            self.serial_.write(b'0\n')
            self.get_logger().info('ROS 2 -> Serial: 0')


def main(args=None):
    rclpy.init(args=args)
    node = SerialBridge()
    rclpy.spin(node)
    node.serial_.close() #Es importante el cerrar correctamente la conexion con el puerto serial
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial

class JoystickPublisher(Node):
    def __init__(self):
        super().__init__('joystick_publisher')
        self.publisher_Y_ = self.create_publisher(Int32,'/joystick_Y',10)
        self.publisher_X_ = self.create_publisher(Int32,'/joystick_X',10) 
        self.serial_ = serial.Serial('/dev/ttyUSB0',115200, timeout = 1)
        #creamos un publicador en el topico joystick
        self.timer_ = self.create_timer(0.01, self.read_serial) #hay que revisar el puerto
        self.get_logger().info('ESP32 conectada')
 
    def read_serial(self):
     if self.serial_.in_waiting > 0: #si hay datos esperando en el puerto serial 
      linea = self.serial_.readline().decode().strip() #lee nuestra linea del serial  los convertimos a un string de python y le quitamos los espacios en blanco 
      partes = linea.split(',')
      textoX = int(partes[0])
      textoY = int(partes[1])
      msgX = Int32()
      msgY = Int32()
      msgX.data = textoY
      msgY.data = textoX
      self.publisher_X_.publish(msgX)
      self.publisher_Y_.publish(msgY)

def main(args = None):
    rclpy.init(args=args)
    node = JoystickPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

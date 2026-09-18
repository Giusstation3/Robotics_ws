import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import serial

#En vez de recibir de ROs2 y mandar al serial, lee del puerto serial y los publica hacia ros2 en el topico analog 
class AnalogSerialPublisher(Node):
    def __init__(self):
        super().__init__('analog_serial_pub')
	#creamos un publicador en el topico analog y abrimos el mismo puerto serial 
        self.publisher_ = self.create_publisher(Int32,'/analog', 10)
        self.serial_ = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        self.timer_ = self.create_timer(0.01, self.read_serial) #hay que revisar el puerto serial muy segudo para no perder datos que llegan del esp32 es el polling 
        self.get_logger().info('ESP32 conectada')

    def read_serial(self):
        if self.serial_.in_waiting > 0: #si hay datos esperando en el puerto serial 
            linea = self.serial_.readline().decode().strip() #lee nuestra linea del serial  los convertimos a un string de python y le quitamos los espacios en blanco 

            if linea.isdigit(): #checamos que si sea un número y lo convertimos a int si es así. y publicamos en analog
                valor = int(linea)
                msg = Int32()
                msg.data = valor
                self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = AnalogSerialPublisher()
    rclpy.spin(node)
    node.serial_.close()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

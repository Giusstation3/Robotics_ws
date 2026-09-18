import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

#solo sirve para subscribirse al topico analog que publica el analog serial pub  y lo imprime en la consola 
class AnalogSubscriber(Node):
    def __init__(self):
        super().__init__('analog_subscriber')

        self.subscription_ = self.create_subscription(Int32, '/analog', self.analog_callback, 10)
        self.get_logger().info('Esperando datos')

    def analog_callback(self, msg):
        valor = msg.data
        self.get_logger().info(f'ADC = {valor}')
	#entonces adc_pot  lee el pin analog, analog serial pub lee serial y publica a ros2, analog subs se subscribe y meustra el valor 

def main(args=None):
    rclpy.init(args=args)
    node = AnalogSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

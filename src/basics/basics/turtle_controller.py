import rclpy
from rclpy.node import Node 
from std_msgs.msg import Int32 
from geometry_msgs.msg import Twist

#Defino el centro de acuerdo a lo que observer en el serial output 
CENTRO = 1800
ZONA_MUERTA = 0.10
VEL_LINEAL_MAX = 2.0
VEL_ANGULAR_MAX = 2.0
SIGNO_LINEAL = 1.0
SIGNO_ANGULAR = -1.0

class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.valor_x = CENTRO
        self.valor_y = CENTRO
	#Creamos el subscriptor para ambos publisher de ejes 
        self.subscription_X = self.create_subscription(
            Int32, '/joystick_X', self.callback_x, 10)
        self.subscription_Y = self.create_subscription(
            Int32, '/joystick_Y', self.callback_y, 10)
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.05, self.publish_cmd)

    def callback_x(self, msg):
        self.valor_x = msg.data

    def callback_y(self, msg):
        self.valor_y = msg.data
#Lo normalizamos para que sea un valor entre -1 y 1 y ademas como la zona muerta es 10 por ciento necesitamos que sea asi 
    def normalizar(self, valor):
        n = (valor - CENTRO) / CENTRO
        n = max(-1.0, min(1.0, n))
        if abs(n) < ZONA_MUERTA:
            return 0.0
        signo = 1.0 if n > 0 else -1.0
        return signo * (abs(n) - ZONA_MUERTA) / (1.0 - ZONA_MUERTA)
#envuamois los valores usando twist 
    def publish_cmd(self):
        x = self.normalizar(self.valor_x)
        y = self.normalizar(self.valor_y)
        msg = Twist()
        msg.linear.x = SIGNO_LINEAL * y * VEL_LINEAL_MAX
        msg.angular.z = SIGNO_ANGULAR * x * VEL_ANGULAR_MAX
        self.publisher_.publish(msg)
        self.get_logger().info(
            f'X={self.valor_x} Y={self.valor_y} '
            f'lin={msg.linear.x:.2f} ang={msg.angular.z:.2f}')


def main(args=None):
    rclpy.init(args=args)
    node = TurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

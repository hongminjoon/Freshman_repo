import rclpy 
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import csv


class Helloworld2_Subscriber(Node):
    def __init__(self):
        super().__init__('Helloworld2_subscriber')
        qos_profile = QoSProfile(depth=10)
        self.helloworld2_subscriber = self.create_subscription(
            String,
            'parsing_data',
            self.subscribe_topic_message2,
            qos_profile)
    
    def subscribe_topic_message2(self, msg: String):
        print(msg.data)
    
def main(args=None):
    rclpy.init(args=args)
    node = Helloworld2_Subscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
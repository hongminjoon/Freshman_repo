import rclpy 
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import csv


class node3_subscriber(Node):
    def __init__(self):
        super().__init__('Node3')
        qos_profile = QoSProfile(depth=10)
        self.Node3_subscriber = self.create_subscription(
            String,
            'parsing_data',
            self.subscribe_topic_message2,
            qos_profile)
    
    def subscribe_topic_message2(self, msg: String):
        print(msg.data)
    
def main(args=None):
    rclpy.init(args=args)
    node3 = node3_subscriber()
    try:
        rclpy.spin(node3)
    except KeyboardInterrupt:
        node3.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node3.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
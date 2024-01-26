# reference blog
# https://www.robotstory.co.kr/king/?mode=view&board_pid=885

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

import serial

class Pub(Node):
    def __init__(self):
        super().__init__('node1')
        qos_profile = QoSProfile(depth=10)
        self.publisher_ = self.create_publisher(String, 'nmea_data', qos_profile)
        timer_period = 2
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        # NMEA.txt 파일 읽기
        file_path = '/home/sjjung/Desktop/vilab/nmea.txt'
        with open(file_path, 'r') as file:
            for line in file:
                nmea_data_msg = String(data=line.strip())
                self.publisher_.publish(nmea_data_msg)
                self.get_logger().info('Publishing: %s' % nmea_data_msg)
        
                

def main(args=None):
    rclpy.init(args=args)
    node = Pub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

    

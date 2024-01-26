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
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.serial_port = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=1)

    def timer_callback(self):
        # NMEA.txt 파일 읽기
        # file_path = '/home/sjjung/Desktop/vilab/nmea.txt'
        # with open(file_path, 'r') as file:
        #     for line in file:
        #ser = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=1)
        ser_data = self.serial_port.readline().decode('utf-8')        # 각 줄의 내용을 std_msgs/String 메시지로 변환
        nmea_data_msg = String(data=ser_data.strip())
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

    

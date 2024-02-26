#sub
import rclpy
import csv 
import os
import pandas
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import pyproj
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

class node2_subscriber(Node):
    def __init__(self):
        super().__init__('Node2')
        qos_profile = QoSProfile(depth=10)
        self.Node2_subscriber = self.create_subscription(String, 'nmea_data', self.parsing, qos_profile)
        self.Node2_publisher = self.create_publisher(String, 'parsing_data', qos_profile)
       
           
    def parsing(self,msg : String):
        #lines = msg.data.split('\n')
        #좌표 변환 함수
        #nmea 위경도는 도분으로 돼 있는데 이를 도분초로 변경하여 도로 바꿈
        if not msg.data:
            msg.data = ""  # 빈 문자열인 경우 그대로 빈 문자열로 처리
        def transform(latitude,longitude):
            try:
                latitude = (float(latitude) // 100) + ((float(latitude) % 100) / 60) + ((float(latitude)%1)*60)/3600 # 도분초->도로 변환 (60->10진법으로 변환)
                longitude = (float(longitude) // 100)+ ((float(longitude) % 100) / 60) + ((float(longitude)%1)*60)/3600  # 경도

                proj_4326 = pyproj.Proj(init = 'epsg:4326')
                proj_32652 = pyproj.Proj(init = 'epsg:32652')  # UTM zone 설정 필요

                utm_easting, utm_northing = pyproj.transform(proj_4326,proj_32652,longitude, latitude)

                return utm_easting,utm_northing
            except ValueError:
                return None,None

        if msg.data[3:6]=='GGA':
            splited_list = msg.data.split(',')
            splited_list[4],splited_list[2] = transform(splited_list[2],splited_list[4]) 
            parsed_data = String()
            parse_data = ( 
                '----------GGA DATA----------\n'
                '{15}\n'
                'GGA.message_id : {0} \n'
                 'GGA.utc : {1} \n'
                 'GGA.lat : {2}\n'
                 'GGA.lat_dir : {3}\n'
                 'GGA.lon : {4}\n'
                 'GGA.lon_dir : {5}\n'
                 'GGA.quality : {6}\n'
                 'GGA.num_satelite : {7}\n'
                 'GGA.HDOP : {8}\n'
                 'GGA.alt : {9}\n'
                 'GGA.alt_unit : {10}\n'
                 'GGA.sep : {11}\n'
                 'GGA.sep_unit : {12}\n'
                 'GGA.diff_age : {13}\n'
                 'GGA.check_sum : {14}\n'
                ).format(splited_list[0],splited_list[1],splited_list[2],splited_list[3],splited_list[4],splited_list[5],splited_list[6],splited_list[7],splited_list[8],splited_list[9],splited_list[10],splited_list[11],splited_list[12],splited_list[13],splited_list[14],msg.data)
            parsed_data.data = parse_data
            self.Node2_publisher.publish(parsed_data)
            soda = {'UTM_X': [splited_list[2]], 'UTM_Y': [splited_list[4]]}
            
            df = pandas.DataFrame(soda)
            if not os.path.exists('output.csv'):
                df.to_csv('output.csv', index=False, mode='w', encoding='utf-8-sig')
            else:
                df.to_csv('output.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
def main(args=None):
    rclpy.init(args=args)
    node2 = node2_subscriber()
    try:
        rclpy.spin(node2)
    except KeyboardInterrupt:
        node2.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node2.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
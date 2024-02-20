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

class HelloworldSubscriber(Node):
    def __init__(self):
        super().__init__('Helloworld_subscriber')
        qos_profile = QoSProfile(depth=10)
        self.helloworld_subscriber = self.create_subscription(
            String,
            'nmea_data',
            self.parsing,
            qos_profile)
        
        self.node2_publisher = self.create_publisher(String, 'parsing_data', qos_profile)
       
           
    def parsing(self,msg : String):
        #lines = msg.data.split('\n')
        #좌표 변환 함수
        if not msg.data:
            msg.data = ""  # 빈 문자열인 경우 그대로 빈 문자열로 처리
        def transform(latitude,longtitude):
            try:
                latitude = float(latitude)//100 +(float(latitude)%100)/60  # 북위 48도 07.038분 위도
                longtitude =  float(longtitude)//100 + (float(longtitude)%100)/60  #경도

                proj_4326 = pyproj.Proj(init = 'epsg:4326')
                proj_32652 = pyproj.Proj(init = 'epsg:32652')  # UTM zone 설정 필요

                utm_easting, utm_northing = pyproj.transform(proj_4326,proj_32652,longtitude, latitude)

                return utm_easting,utm_northing
            except ValueError:
                return None,None

        if msg.data[3:6]=='GGA':
            list = msg.data.split(',')
            list[4],list[2] = transform(list[2],list[4]) 
            temp = String()
            a = ( 
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
                ).format(list[0],list[1],list[2],list[3],list[4],list[5],list[6],list[7],list[8],list[9],list[10],list[11],list[12],list[13],list[14],msg.data)
            temp.data = a
            soda = {'UTM_X': [list[4]], 'UTM_Y': [list[2]]}
            
            df = pandas.DataFrame(soda)
            if not os.path.exists('output.csv'):
                df.to_csv('output.csv', index=False, mode='w', encoding='utf-8-sig')
            else:
                df.to_csv('output.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
            '''
            #하나씩만 출력할 경우
            f = open('lo.csv','w')
            data = [list[2], list[4]]
            writer = csv.writer(f)
            writer.writerow(data)
            '''
            self.node2_publisher.publish(temp)
               
    
def main(args=None):
    rclpy.init(args=args)
    node = HelloworldSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
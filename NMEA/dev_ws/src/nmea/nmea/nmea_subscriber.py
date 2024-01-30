import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String

import pyproj
import pynmea2
import pandas as pd

import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

class Sub(Node):
    def __init__(self):
        super().__init__('node2')
        qos_profile = QoSProfile(depth=10)
        self.subscriber_ = self.create_subscription(
            String,
            'nmea_data',
            self.listener_callback,
            qos_profile
        )
        
        self.publisher_ = self.create_publisher(String, 
                            'parsed_data', qos_profile)
        
        self.latitude_list = []
        self.longitude_list = []

        self.UTM_latitude_list = []
        self.UTM_longitude_list = []
    
    
    def listener_callback(self, msg):
        if msg.data[3:6] == "GGA":
            # GGA 데이터를 프로세싱
            latitude, longitude, utm_latitude, utm_longitude = self.TM2UTM(msg.data)
            
            # latitude, longitude 0값 예외 처리
            if latitude and longitude: 
                self.UTM_latitude_list.append(utm_latitude)
                self.UTM_longitude_list.append(utm_longitude)

            line_list = msg.data.split(',')

            result_str = (
                    "\n"
                    "---------------GGA DATA----------------\n"
                    "GGA.raw_data : {}\n"
                    "GGA.message_id : {}\n"
                    "GGA.utc : {}\n"
                    "GGA.lat : {}\n"
                    "GGA.lat_dir : {}\n"
                    "GGA.utm_lat : {}\n"
                    "GGA.lon : {}\n"
                    "GGA.lon_dir : {}\n"
                    "GGA.utm_lon : {}\n"
                    "GGA.quality : {}\n"
                    "GGA.num_satelite : {}\n"
                    "GGA.HDOP : {}\n"
                    "GGA.alt : {}\n"
                    "GGA.alt_unit : {}\n"
                    "GGA.sep : {}\n"
                    "GGA.sep_unit : {}\n"
                    "GGA.diff_age : {}\n"
                    "GGA.diff_station : {}"
                ).format(
                    msg.data.strip(),
                    line_list[0],
                    line_list[1],
                    latitude,
                    line_list[3],
                    utm_latitude,
                    longitude,
                    line_list[5],
                    utm_longitude,
                    line_list[6],
                    line_list[7],
                    line_list[8],
                    line_list[9],
                    line_list[10],
                    line_list[11],
                    line_list[12],
                    line_list[13],
                    line_list[14]
            )

            result_string = String(data=result_str)
            # 프로세싱된 GGA 데이터를 퍼블리시
            self.publisher_.publish(result_string)
    
    def TM2UTM(self, gga_sentence):
        # Parse GGA sentence
        msg = pynmea2.parse(gga_sentence)

        latitude = float(msg.latitude) if msg.lat_dir == 'N' else -float(msg.latitude)
        longitude = float(msg.longitude) if msg.lon_dir == 'E' else -float(msg.longitude)
        
        proj_4326 = pyproj.Proj(init='epsg:4326')
        proj_32652 = pyproj.Proj(init='epsg:32652')

        utm_longitude, utm_latitude = pyproj.transform(proj_4326,proj_32652,longitude, latitude)

        return latitude, longitude, utm_latitude, utm_longitude
    
    def save_to_csv(self):
        data = {'UTM_latitude': self.UTM_latitude_list, 'UTM_longitude': self.UTM_longitude_list}
        df = pd.DataFrame(data)
        df.to_csv('utm_data.csv', index=False)
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = Sub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.save_to_csv()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

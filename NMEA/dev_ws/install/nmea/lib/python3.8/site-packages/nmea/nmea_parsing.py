# reference: https://www.robotstory.co.kr/king/?board_page=3&vid=884

import rclpy
from rclpy.node import Node

import pyproj
import pynmea2

class NmeaNode(Node):
    def __init__(self, filename):
        super().__init__('nmea_node')
        self.filename = filename
    
    def info(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            if line[3:6] == "GGA":
                line_list = line.split(',')

                print("---------------GGA DATA----------------")
                print("GGA.raw_data : %s" % line.strip())
                print("GGA.message_id : %s" % line_list[0])
                print("GGA.utc : %s" % line_list[1])

                latitude, longitude = self.TM2UTM(line)

                print("GGA.lat : %s" % latitude)
                print("GGA.lat_dir : %s" % line_list[3])
                print("GGA.lon : %s" % longitude)
                print("GGA.lon_dir : %s" % line_list[5])
                print("GGA.quality : %s" % line_list[6])
                print("GGA.num_satellite : %s" % line_list[7])
                print("GGA.HDOP : %s" % line_list[8])
                print("GGA.alt : %s" % line_list[9])
                print("GGA.alt_unit : %s" % line_list[10])
                print("GGA.sep : %s" % line_list[11])
                print("GGA.sep_unit : %s" % line_list[12])
                print("GGA.diff_age : %s" % line_list[13])
                print("GGA.diff_station : %s" % line_list[14])

    # Convert to UTM coordinate
    def TM2UTM(self, gga_sentence):
        # Parse GGA sentence
        msg = pynmea2.parse(gga_sentence)

        latitude = float(msg.latitude) if msg.lat_dir == 'N' else -float(msg.latitude)
        longitude = float(msg.longitude) if msg.lon_dir == 'E' else -float(msg.longitude)

        return latitude, longitude


def main(args=None):
    rclpy.init(args=args)

    try:
        nmea_node = NmeaNode('/home/user/Desktop/vilab/nmea.txt')
        nmea_node.info()
        rclpy.spin(nmea_node)
    except KeyboardInterrupt:
        pass
    finally:
        nmea_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

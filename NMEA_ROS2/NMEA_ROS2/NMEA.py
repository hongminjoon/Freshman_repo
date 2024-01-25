import serial
import csv
import pyproj

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NMEA(Node):
    def __init__(self, serial_port='/dev/ttyACM0', baudrate=115200, timeout=1.0) -> None:
        super().__init__('NMEA')

        self.ser = serial.Serial(serial_port, baudrate, timeout=timeout)
        self.type = '$GNGGA'
        self.decodetype = 'utf-8'

        self.proj_wgs84 = pyproj.Proj(init='epsg:4326')  # WGS84 coordinate system
        self.proj_utm = pyproj.Proj(init='epsg:32652')  # UTM coordinate system

        self.pub = self.create_publisher(String, 'nmea_data', 10)
        self.timer = self.create_timer(0.1, self.read_serial)

    def read_serial(self):
        while True:
            data = self.ser.readline().decode(self.decodetype)
            if data.startswith(self.type):
                try:
                    gga_data = self.parsing(data)
                    if self.cheak_data(gga_data):
                        self.output(gga_data)
                        self.pub_msg(gga_data)
                        self.save_csv(gga_data)
                except Exception as e:
                    pass

    def parsing(self, data):
        fields = data.split(',')
        gga_data = {
            'raw_data' : data,
            'message_id': fields[0][1:],
            'utc': fields[1],
            'lat': float(fields[2][:2]) + float(fields[2][2:]) / 60.0 if fields[2] else None,
            'lat_dir': fields[3],
            'lon': float(fields[4][:3]) + float(fields[4][3:]) / 60.0 if fields[4] else None,
            'lon_dir': fields[5],
            'gps_qual': int(fields[6]),
            'num_sats': int(fields[7]),
            'altitude': float(fields[9]),
            'altitude_units': fields[10],
            'geo_sep': float(fields[11]),
            'geo_sep_units': fields[12],
            'age_gps_data': fields[13],
            'ref_station_id': fields[14][:4],
            'check_sum': fields[14][5:]
        }
        return gga_data
        
    def cheak_data(self, gga_data):
        if 'lat' in gga_data and 'lon' in gga_data and 'gps_qual' in gga_data and 'num_sats' in gga_data:
            return True
        else:
            return False

    def output(self, gga_data):
        print("------- GGA DATA -------\n")
        print(f'GGA.raw_data : {gga_data["raw_data"]}', end='')
        print(f'GGA.message_id : {gga_data["message_id"]}')
        print(f'GGA.utc : {gga_data["utc"]}')
        print(f'GGA.lat : {gga_data["lat"]}')
        print(f'GGA.lat_dir : {gga_data["lat_dir"]}')
        print(f'GGA.lon : {gga_data["lon"]}')
        print(f'GGA.lon_dir : {gga_data["lon_dir"]}')
        print(f'GGA.quality : {gga_data["gps_qual"]}')
        print(f'GGA.num_satellite : {gga_data["num_sats"]}')
        print(f'GGA.alt : {gga_data["altitude"]}')
        print(f'GGA.alt_unit : {gga_data["altitude_units"]}')
        print(f'GGA.sep : {gga_data["geo_sep"]}')
        print(f'GGA.sep_unit : {gga_data["geo_sep_units"]}')
        print(f'GGA.diff_age : {gga_data["age_gps_data"]}')
        print(f'GGA.diff_station : {gga_data["ref_station_id"]}')
        print(f'GGA.check_sum : {gga_data["check_sum"]}', end='')
        print("\n------------------------\n")
    
    def pub_msg(self, gga_data):
        utm_y, utm_x = pyproj.transform(self.proj_wgs84, self.proj_utm, gga_data['lon'], gga_data['lat'])
        msg = String()
        msg.data = f'UTM_X: {utm_x}, UTM_Y: {utm_y}'
        self.pub.publish(msg)

    def save_csv(self, gga_data):
        utm_y, utm_x = pyproj.transform(self.proj_wgs84, self.proj_utm, gga_data['lon'], gga_data['lat'])
        file_path = 'NMEA.csv'
        fieldnames = ['UTM_X', 'UTM_Y']

        with open(file_path, mode='a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({
                'UTM_X' : utm_x,
                'UTM_Y' : utm_y
            })
        

def main(args=None):
    rclpy.init(args=args)
    node = NMEA()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally: 
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()

import rclpy
from rclpy.node import Node
from gps_cstm_msgs.msg import GpsData
import os
import serial
import re

class Parpub(Node):
    def __init__(self):
        super().__init__('par_pub')
        self.par_pub = self.create_publisher(GpsData, 'gps_serial' ,10)
        self.time_between = 0.5
        self.timer = self.create_timer(self.time_between, self.serial_publish)
        self.time = 0
        self.data_name = ['gps_type', 'time', 'lat', 'NS', 'lon', 'EW', 'quality', 'numSV', 'HDOP', 'alt', 'altUnit', 'sep', 'sepUnit', 'diffAge', 'diffStation', 'cs']
        self.p = re.compile('\$[\w]{2}(?P<gps_type>[\w]*)\,(?P<time>[\d\.]*)\,(?P<lat>[\d\.]*)\,(?P<NS>[\w]*)\,(?P<lon>[\d\.]*)\,(?P<EW>[\w]*)\,(?P<quality>\d)\,(?P<numSV>\d*)\,(?P<HDOP>[\d\.]*)\,(?P<alt>[\d\.]*)\,(?P<altUnit>\w*)\,(?P<sep>[\d\.]*)\,(?P<sepUnit>[\w]*)\,(?P<diffAge>[\d\.]*)\,(?P<diffStation>[\d]*)\*(?P<cs>[\w]*)')

        if self.time == 0:
            self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout = 1)
            # /dev 디렉토리에서 gps가 연결된 usb 포트를 확인 후 바꾸어주어야 함 
            
    def serial_publish(self):
        self.time += 1
        
        gps_line = self.ser.readlines()[-2].decode() #이거 안되면 진짜 모름
        
        gps_msg = GpsData()

        if gps_line[3:6] == 'GGA':
            try:
                gps_msg.gpstype = self.p.match(gps_line).group('gps_type')
                gps_msg.time = self.p.match(gps_line).group('time')
                gps_msg.lat = self.p.match(gps_line).group('lat')
                gps_msg.ns = self.p.match(gps_line).group('NS')
                gps_msg.lon = self.p.match(gps_line).group('lon')
                gps_msg.ew = self.p.match(gps_line).group('EW')
                gps_msg.quality = self.p.match(gps_line).group('quality')
                gps_msg.numsv = self.p.match(gps_line).group('numSV')
                gps_msg.hdop = self.p.match(gps_line).group('HDOP')
                gps_msg.alt = self.p.match(gps_line).group('alt')
                gps_msg.altunit = self.p.match(gps_line).group('altUnit')
                gps_msg.sep = self.p.match(gps_line).group('sep')
                gps_msg.sepunit = self.p.match(gps_line).group('sepUnit')
                gps_msg.diffage = self.p.match(gps_line).group('diffAge')
                gps_msg.diffstation = self.p.match(gps_line).group('diffStation')
                gps_msg.cs = self.p.match(gps_line).group('cs')
            except AttributeError:
                pass
            # custom message 의 .msg 파일에서 선언한 변수형에 따라 변환해줘야함 지금은 모두 string (데이터가 ''일 때 다른 변수형태로 변환하면 에러).
            # regex match 시 위에서 정의한 표현식에 일치하지 않는 serial data가 존재(NoneType error). 지금은 try: except:로 regex에 일치하는 gga 메시지 형태만 전달하도록 설정.
            # 반복문으로 바꿀 방법?
            
        else:
            pass
            

        
        os.system('clear')
        print('publishing..')
        self.par_pub.publish(gps_msg)
        
        # =========for msg identification=========
        # print(gps_msg.gpstype, gps_msg.time,gps_msg.lat,gps_msg.ns,gps_msg.lon,gps_msg.ew,gps_msg.quality,gps_msg.numsv,gps_msg.hdop,gps_msg.alt,gps_msg.altunit,gps_msg.sep,gps_msg.sepunit,gps_msg.diffage,gps_msg.diffstation, gps_msg.cs)
        
def main(args = None):
    rclpy.init(args = args)
    try:
        parpub = Parpub()
        try:
            rclpy.spin(parpub)
        except KeyboardInterrupt:
            os.system('clear')
            print('===keyboard inturrupt===')
        finally:
            parpub.destroy_node()
    finally :
        rclpy.shutdown()

if __name__ == '__main__':
    main()

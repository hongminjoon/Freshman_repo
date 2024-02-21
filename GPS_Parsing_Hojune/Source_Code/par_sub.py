import rclpy
from rclpy.node import Node
from gps_cstm_msgs.msg import GpsData
import os
import pyproj
import pandas

class Parsub(Node):
    def __init__(self):
        super().__init__('par_sub')
        self.par_sub = self.create_subscription(GpsData, 'gps_serial', self.serial_subscribe, 10)
        self.time = 0
        self.data_name = ['gps_type', 'time', 'lat', 'NS', 'lon', 'EW', 'quality', 'numSV', 'HDOP', 'alt', 'altUnit', 'sep', 'sepUnit', 'diffAge', 'diffStation', 'cs']
        
        if 'gps_data.csv' in os.listdir(os.getcwd()):
            self.frame = pandas.read_csv('gps_data.csv')
            self.frame_line = len(self.frame)-1
        else:       
            self.frame = pandas.DataFrame([],columns = ['NMEA lon', 'NMEA lat', 'UTM x', 'UTM y','time'])
            self.frame_line = 0
        # 'gps_data.csv' 라는 nmea / UTM 좌표가 저장된 스프레드시트 파일이 있을 시 프레임을 가져옴 (os 모듈)
        # 그렇지 않을 때 새 frame을 생성(pandas 라이브러리)
        
        
        
        self.NMEA_to_UTM = pyproj.Transformer.from_crs('epsg:4326', 'epsg:32652', always_xy = True).transform
        # epsg:4326 - NMEA 0183(decimal degree), epsg:32652 - UTM coordinates (pyproj 라이브러리)



    def serial_subscribe(self, gps_msg):
        self.time += 1
        gps_msg_list = [gps_msg.gpstype, gps_msg.time, gps_msg.lat, gps_msg.ns, gps_msg.lon, gps_msg.ew, gps_msg.quality, gps_msg.numsv, gps_msg.hdop, gps_msg.alt, gps_msg.altunit, gps_msg.sep, gps_msg.sepunit, gps_msg.diffage, gps_msg.diffstation, gps_msg.cs]
        if gps_msg.gpstype == 'GGA':
            
            os.system('clear')
            print('=' * 15, 'line : {0}'.format(self.time),'\n')
            # =============== line : n
            
            for i in range(len(gps_msg_list)):
                print(self.data_name[i], ' ' * (15 - len(self.data_name[i])),':', gps_msg_list[i])
                # 데이터 이름 : 데이터 값 
            
            if gps_msg.lon and gps_msg.lat != '':
                Ulon = float(gps_msg.lon[0 : gps_msg.lon.index('.') - 2]) + (float(gps_msg.lon[gps_msg.lon.index('.') -2 : ])/60)
                Ulat = float(gps_msg.lat[0 : gps_msg.lat.index('.') - 2]) + (float(gps_msg.lat[gps_msg.lat.index('.') - 2 : ])/60)
                #nmea 0183 의 ddmm.mm 형식을 deciaml degree 형태로 변환. float 형으로 변환하여 연산
            
                Ulon, Ulat = self.NMEA_to_UTM(Ulon, Ulat)
                
                self.frame.loc[self.frame_line] = [gps_msg.lon, gps_msg.lat, Ulon, Ulat, gps_msg.time]
                self.frame_line += 1
                # 프레임에 nmea / UTM 좌표를 기록한 새 행을 추가하고 행index + 1
                
            print(self.frame)
            if 'gpsdata.csv' in os.listdir(os.getcwd()):
                self.frame.to_csv('gps_data.csv', mode = 'a', header = False, index = False)
                
                # Node가 실행된 경로에 UTM gps 데이터 저장
                # mode = 'a'로 기존 정보에 덮어쓰기
                # index를 False로 저장해야 index 열(0,1,2,3..)이 저장되지 않아 다시 불러왔을 때 열의 개수가 맞지 않는 Value error를 발생시키지 않는다.
                
            else:
                self.frame.to_csv('gps_data.csv', index = False)
                

        else:
            pass
        
        # =========for msg identification=========
        # print(gps_msg.gpstype, gps_msg.time,gps_msg.lat,gps_msg.ns,gps_msg.lon,gps_msg.ew,gps_msg.quality,gps_msg.numsv,gps_msg.hdop,gps_msg.alt,gps_msg.altunit,gps_msg.sep,gps_msg.sepunit,gps_msg.diffage,gps_msg.diffstation, gps_msg.cs)

def main(args =None):
    rclpy.init(args =args)
    try:
        parsub = Parsub()
        try:
            rclpy.spin(parsub)
        except KeyboardInterrupt:
            # os.system('clear')
            print('===keyboard inturrupt===')
        finally:
            parsub.destroy_node()
    finally:
        rclpy.shutdown()

if __name__ == '__main__ ':
    main()
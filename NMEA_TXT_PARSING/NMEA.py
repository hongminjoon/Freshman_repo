import pyproj
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

class parsing:
    #nmea.txt 받아내는 함수
    def __init__(self):
        f = open("/home/hyeeun/inf/nmea.txt", 'r')
        self.lines = f.readlines()
        self.GGA_list = []
    
    # Transform UTM
    def transform(self, latitude, longitude):
        latitude = float(latitude) // 100 + (float(latitude) % 100) / 60  # 북위 48도 07.038분 위도
        longitude = float(longitude) // 100 + (float(longitude) % 100) / 60  # 경도

        proj_4326 = pyproj.Proj(init='epsg:4326')
        proj_32652 = pyproj.Proj(init='epsg:32652')  # UTM zone 설정 필요

        utm_easting, utm_northing = pyproj.transform(proj_4326, proj_32652, longitude, latitude)
        return utm_easting, utm_northing

    #파싱 데이터 추출 함수
    def print_parsing_data(self):
        # GGA_list에 GGA 데이터만 담기
        for line in self.lines:
            if not line: break
            if line[3:6] == 'GGA':
                self.GGA_list.append(line)

        # 분할 및 출력
        for list in self.GGA_list:
            list_print = list
            list_print = list_print.strip('\n')
            list = list[1:].strip('\n')  # 앞에 $제거 && 개행문자 제거하여 쓸데없는 줄바꿈 없애기
            list = list.split(',')  # ,에 따라 분할
            list[4], list[2] = self.transform(list[2], list[4])
            print('----------GGA DATA----------')
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
            ).format(list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7], list[8], list[9],
                     list[10], list[11], list[12], list[13], list[14], list_print)
            self.a = a
            print(a)

def main():
    NMEA_PARSING = parsing()
    NMEA_PARSING.print_parsing_data()
    

if __name__ == "__main__":
    main()

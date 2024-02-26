import pyproj
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

class parsing:
    #nmea.txt 읽기모드로 불러오는 함수
    def __init__(self):
        f = open("/home/hyeeun/inf/nmea.txt", 'r')
        self.lines = f.readlines()
        self.GGA_list = [] #GGA 데이터만 담긴 리스트
        
    
    # Transform UTM     
        #nmea 위경도는 도분으로 돼 있는데 이를 도분초로 변경하여 도로 바꿈
    #맨 처음에 나온 gga가 우리 연구실 위경도가 맞는지 확인하기
    def transform(self, latitude, longitude):
        latitude = (float(latitude) // 100) + ((float(latitude) % 100) / 60) + ((float(latitude)%1)*60)/3600 # 도분초->도로 변환 (60->10진법으로 변환)
        longitude = (float(longitude) // 100)+ ((float(longitude) % 100) / 60) + ((float(longitude)%1)*60)/3600  # 경도

        #pyproj.transform(원본좌표계,대상좌표계,경도,위도) 
        proj_4326 = pyproj.Proj(init='epsg:4326') #WSG84좌표 시스템을 의미
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

        for list in self.GGA_list:
            print_list = list #전체 정보가 담긴 GGA 한줄 출력하기 위한 변수
            print_list = print_list.strip('\n')
            splited_list = list[1:].strip('\n')  # 앞에 $제거 && 개행문자 제거하여 쓸데없는 줄바꿈 없애기
            splited_list = splited_list.split(',')  # ,에 따라 분할
            splited_list[4], splited_list[2] = self.transform(splited_list[2], splited_list[4])
            print('----------GGA DATA----------')
            parsed_value = (
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
            ).format(splited_list[0], splited_list[1], splited_list[2], splited_list[3], splited_list[4], splited_list[5], splited_list[6], splited_list[7], splited_list[8], splited_list[9],
                     splited_list[10], splited_list[11], splited_list[12], splited_list[13], splited_list[14], print_list)
            self.parsed_value = parsed_value
            print(parsed_value)

def main():
    NMEA_PARSING = parsing()
    NMEA_PARSING.print_parsing_data()
    

if __name__ == "__main__":
    main()

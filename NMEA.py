import pyproj
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#알게된 점 : 파일 불러오기(readlines) 리스트에 추가하기(append) 특정 문자 제거하기(strip('\n')) 특정문자를 기준으로 분류하기(split()) 반복문에서 2이상 return값 받기(zip())

f = open("/home/hyeeun/inf/nmea.txt", 'r')
lines = f.readlines()
GGA_list = []

#좌표 변환 함수
def transform(latitude,longtitude):
    latitude = float(latitude)//100 +(float(latitude)%100)/60  # 북위 48도 07.038분 위도
    longtitude =  float(longtitude)//100 + (float(longtitude)%100)/60  #경도

    proj_4326 = pyproj.Proj(init = 'epsg:4326')
    proj_32652 = pyproj.Proj(init = 'epsg:32652')  # UTM zone 설정 필요

    utm_easting, utm_northing = pyproj.transform(proj_4326,proj_32652,longtitude, latitude)
    
    return utm_easting,utm_northing

#GGA_list에 GGA 데이터만 담기
for line in lines:
    if not line : break
    if line[3:6]=='GGA':
        GGA_list.append(line)

#분할 및 출력
for list in GGA_list:
    list = list[1:].strip('\n') #앞에 $제거 && 개행문자 제거하여 쓸데없는 줄바꿈 없애기
    print(list)
    list = list.split(',') #,에 따라 분할
    list[4],list[2] = transform(list[2],list[4]) 
    print("GGA.message_id",':',list[0])
    print("GGA.utc",':',list[1])
    print("GGA.lat",':',list[2])
    print("GGA.lat_dir",':',list[3])
    print("GGA.lon",':',list[4])
    print("GGA.lon_dir",':',list[5])
    print("GGA.quality",':',list[6])
    print("GGA.num_satelite",':',list[7])
    print("GGA.HDOP",':',list[8])
    print("GGA.alt",':',list[9])
    print("GGA.alt_unit",':',list[10])
    print("GGA.sep",':',list[11])
    print("GGA.sep_unit",':',list[12])
    print("GGA.diff_age",':',list[13],)
    print("GGA.check_sum",':',list[14])
    
f.close()
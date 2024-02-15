# read_serial.py

import serial

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=1)

try:
    while True:
        # 시리얼 포트에서 데이터 읽기
        data = ser.readline().decode('utf-8').strip()
        
        # 읽은 데이터 출력
        print(data)

except KeyboardInterrupt:
    # Ctrl+C를 누르면 프로그램 종료
    ser.close()
    print("프로그램이 종료되었습니다.")
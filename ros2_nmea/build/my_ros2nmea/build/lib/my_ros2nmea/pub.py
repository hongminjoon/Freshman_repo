import rclpy 
from rclpy.node import Node
from rclpy.qos import QoSProfile
from std_msgs.msg import String
import serial
#노드의 메인 클래스는 헬로퍼블리셔로 Node 클래스를 상속

class HelloworldPublisher(Node): #Node라는 클래스를 상속받은 메인 클래스  헬로월드퍼블리셔 클래스
    def __init__(self):
        super().__init__('helloworld_publisher') #노드 이름
        qos_profile = QoSProfile(depth=10) #버피=10 (10개의 데이터를 저장해주는 느낌)
                                           #ex)12인 경우에 2부터의 값을 보여줄 수 있음
        self.helloworld_publisher = self.create_publisher(String, 'nmea_data', qos_profile)
        #self.file_path = '/home/hyeeun/inf/nmea.txt'
        self.timer = self.create_timer(1, self.serial)
        self.count = 0 #콜백 함수에 사용되는 count
    
    #nmea_txt를 받는 경우
    #def publish_txt(self):
        #with open(self.file_path,'r') as file:
            #txt_content = file.read()
        #msg = String()
        #msg.data = txt_content
        #self.helloworld_publisher.publish(msg)
        #self.get_logger().info('published txt content')    
        
    def serial(self):
        ser = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=1)
        
        while True:
            # 시리얼 포트에서 데이터 읽기
            msg = String()
            msg.data = ser.readline().decode('utf-8').strip()
            #msg_data = ser.read_all()
            self.helloworld_publisher.publish(msg)
            self.get_logger().info('published txt content')    
            
def main(args=None):
    rclpy.init(args=args) #초기화
    txt_publisher = HelloworldPublisher()
    
    try:
        rclpy.spin(txt_publisher) #rclpy.spin함수 이용 ->생성한 노드를spin시켜 지정된 콜백함수 호출
																			#spin :약간 무한반복느낌( 찾아보기 ) 
    except KeyboardInterrupt:
        txt_publisher.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        txt_publisher.destroy_node()
        rclpy.shutdown() #종료
    
    
if __name__ == '__main__': #함수의 이름이 main인 경우 main()호출한다
    main()
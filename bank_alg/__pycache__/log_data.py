import logging

# 로그 파일 설정 (이어쓰기 모드로 설정)
logging.basicConfig(filename='user_data.log', level=logging.INFO, filemode='a')

# 사용자 정보를 저장할 리스트
user_data_list = []

# 사용자 정보를 로그에 저장하고 리스트에도 추가하는 함수
def save_user_data(user_id, password, account, charge):
        
    #user_data = [user_id, password, account, charge]
    #user_data_list.append(user_data)
    logger.info('User ID: %s, Password: %s, Account: %s, Charge: %d', user_id, password, account, charge)
    #print(user_data_list)

# logger 객체 생성
logger = logging.getLogger('user_logger')
logger.setLevel(logging.INFO)



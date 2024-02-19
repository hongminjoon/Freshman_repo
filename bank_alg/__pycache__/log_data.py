import logging
import random

# 로그 파일 설정 (이어쓰기 모드로 설정)
logging.basicConfig(filename='user_data.log', level=logging.INFO, filemode='a')

# 사용자 정보를 로그에 저장
def save_user_data(user_id, password, account, charge):
    logger.info('User ID: %s, Password: %s, Account: %s, Charge: %d', user_id, password, account, charge)

#log 데이터 모두 출력
def print_user_data():
    with open(log_path,'r') as f:
        for line in f:
            print(line.strip())
            
#계좌 송금 -> 잔액 수정       
def modify_log_account(user_id, new_charge):
    with open(log_path, 'r') as f:
        lines = f.readlines()

    with open(log_path, 'w') as f:
        for line in lines:
            if user_id in line:
                parts = line.split(', ')
                for i, part in enumerate(parts):
                    if part.startswith('Charge:'):
                        parts[i] = 'Charge: ' + str(new_charge) + '\n'
                line = ', '.join(parts)
            f.write(line)


def count_lines_in_file(file_path):
    line_count = 0
    with open(file_path, 'r') as f:
        for line in f:
            line_count += 1 #현재 유저 수(log줄 개수)
    random_numbers = random.sample(range(1,line_count+1),2) #주고받는 유저 랜덤 지목 
    #1.random_numbers[0]주는 사람의 한도 내에 랜덤 돌리기
    #2.그만큼 주는 사람의 계좌에서 돈 빼고 (modify 함수)
    #3.그만큼 받는 사람의 계좌에서 돈 더하기 (modify 함수)
    #+)주고받은 내역 어떻게 만들지 생각하기 (엑셀이 나을까나)
        
# logger 객체 생성
logger = logging.getLogger('user_logger')
logger.setLevel(logging.INFO)
# 로그 파일 경로
log_path = 'user_Data.log'

count_lines_in_file(log_path)





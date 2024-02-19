import re

# 로그 파일에서 사용자 정보를 읽어와서 리스트로 반환하는 함수
def parse_log_file(log_file):
    user_data_list = []
    with open(log_file, 'r') as f:
        for line in f:
            # 각 줄에서 "User ID:", "Password:", "Account:", "Charge:"를 찾아서 사용자 정보 추출
            match = re.search(r'User ID: (\S+), Password: (\S+), Account: (\S+), Charge: (\d+)', line)
            if match:
                # 사용자 정보를 추출하여 리스트에 추가
                user_id = match.group(1)
                password = match.group(2)
                account = match.group(3)
                charge = int(match.group(4))
                user_data_list.append([user_id, password, account, charge])
    return user_data_list

# 로그 파일 경로
log_file = 'user_data.log'

# 로그 파일을 파싱하여 사용자 정보를 리스트로 변환
user_data_list = parse_log_file(log_file)

# 결과 출력
print(user_data_list)

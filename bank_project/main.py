import os
from user import User
from log import Log

user_list = []
user = User()

log = Log()
log_file_path = "./log/user_log.txt"
if os.path.exists(log_file_path):
    user_list = log.read_log(log_file_path)

def print_user_list(user_list):
    for i in user_list:
        print(i)

def main():
    while True:
        print("##################################")
        print('Main Menu')
        print("1. User 생성")
        print("2. User 정보")
        print("3. 계좌 전송")
        print("4. User 삭제")
        print("##################################")
        print('종료하시려면 "Exit"를 입력하세요.')
        
        ch = input("번호를 입력하세요: ")
        print("##################################")

        if ch == "1":
            user.createUser()
            id, password, account, deposit = user.get_user()
            user_list.append((id, password, account, deposit))
        elif ch == "2":
            print_user_list(user_list)
        elif ch == "3":
            print(3)
        elif ch == "4":
            id_del, password_del = user.deleteUser()
            print(id_del, password_del)
        elif ch == "Exit":
            print("Exit")
            log.save_log(user_list)
            break
        else:
            print("다시입력")

if __name__ == '__main__':
    main()
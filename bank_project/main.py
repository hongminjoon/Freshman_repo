import user_list
from user import User
from log import Log

user = User()
log = Log()
user_list.loading_user_list()

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
            user_list.append_user_list(id, password, account, deposit)
        elif ch == "2":
            user_list.print_user_list()
        elif ch == "3":
            print(3)
        elif ch == "4":
            # id_del, password_del = user.deleteUser()
            # #print(user_list)
            # login_dict = {username: password for username, password, _, _ in user_list}
            # #print(login_dict)
            # if id_del in login_dict and password_del != login_dict[id_del]:
            #     print("입력하신 id의 비밀번호가 일치하지 않습니다.")
            # elif id_del not in user_list:
            #     print("입력하신 id가 존재하지 않습니다.")
            print(4)

        elif ch == "Exit":
            print("Exit")
            log.save_log(user_list.user_list)
            break
        else:
            print("다시입력")

if __name__ == '__main__':
    main()
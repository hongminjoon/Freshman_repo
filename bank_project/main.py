import user_list
from user import User
from log import Log
from bank_system import Bank_System

user = User()
log = Log()
bank = Bank_System()
user_list.loading_user_list()
bank.loading_user_list()

def main():
    while True:
        print("##################################")
        print('Main Menu')
        print("1. User 생성")
        print("2. User 정보")
        print("3. 계좌 전송")
        print("4. 계좌 조회")
        print("5. User 삭제")
        print("##################################")
        print('종료하시려면 "Exit"를 입력하세요.')
        
        ch = input("번호를 입력하세요: ")
        print("##################################")

        if ch == "1":
            a = user.createUser()
            if a is not None:
                id, password, account, deposit = user.get_user()
                user_list.append_user_list(id, password, account, deposit)
            
        elif ch == "2":
            user_list.print_user_list()

        elif ch == "3":
            if user_list.get_user_num() > 1:
                bank.transfer_money()
            else:
                print("최소 인원 2명이 되지 않습니다.")
            
        elif ch == "4":
            account = input("조회할 계좌번호를 입력하세요: ")
            history = bank.get_account_history(account)
            if history is not None:
                print(history)

        elif ch == "5":
            id_del, password_del, account_del = user.deleteUser()

            if id_del != " " and password_del != " ":
                user_list.delete_user(id_del, password_del)
            if account_del != " ":
                bank.delete_bank(account_del)

        elif ch == "Exit":
            print("Exit")
            log.save_user_log(user_list.user_list)
            log.save_bank_log(bank.get_bank_dic())
            break

        else:
            print("다시입력")

if __name__ == '__main__':
    main()
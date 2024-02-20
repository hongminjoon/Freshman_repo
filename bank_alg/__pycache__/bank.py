from service import *
from log_data import *

def main():
    push = "ab"
    while push != "Exit":
        push = input("사용할 서비스 번호를 입력해주세요 : ")
        if push == "1":
            user = One()
            if user.create_id():
                if user.create_pw():
                    user.create_ac()
                    user.charge = 100000
                    print("회원가입이 완료되었습니다 !")
            else :
                push =  input("사용할 서비스 번호를 다시 입력해주세요 : ")
            save_user_data(user.id,user.pw,user.ac,user.charge)
            
                    
        if push == "2":
            print_user_data()
            
        if push == "3":
            modify_log_account('hyeeun1116',30000)
            with open('user_data.log', 'r') as f:
                for line in f:
                    print(line.strip())  # 각 줄의 앞뒤 공백 제거 후 출력
        #3번 입력 시 랜덤으로 계좌 전송 ()
        #4번 입력 시 유저 삭제 기능 실행

if __name__ == "__main__" :
    main()
    
#문제점 : 계좌번호까지 마치면 ID입력으로 다시감 ->디버깅해서 알아보기 (service로 다시 가는거같음)
#문제점 : 계좌번호까지 마치면 ID입력으로 다시감 ->디버깅해서 알아보기 (service로 다시 가는거같음)

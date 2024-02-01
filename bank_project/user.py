import re 

class User:

    def __init__(self):
        self.id = ''
        self.password = ''
        self.account = 0
        self.deposit = 100000

    def createUser(self):
        self.createId()
        # 수정 필요
        # if id가 None이 아니면 createPassword()
        # if id가 None이면, 메인메뉴로 이동
        self.createPassword()
        self.createAccount()

    def createId(self):
        max_attempts = 3
        attempts = 0
        
        while attempts < max_attempts:
            id = input("아이디를 입력하세요: ")
            if self.check_id_format(id):
                self.id = id
                return id
            else:
                print("오류: 아이디는 영어 및 숫자 조합이어야 하며, 최소 6자 이상이어야 합니다.")
                attempts += 1
        
        print(f"{max_attempts}회 이상 오류가 발생하여 기능을 종료합니다.")
        return None
        
    def createPassword(self):   
        while True:
            password = input("비밀번호를 입력하세요: ")
            confirm_password = input("비밀번호를 한번 더 입력하세요: ")

            if password != confirm_password:
                print("비밀번호가 일치하지 않습니다.")
                continue

            elif password == confirm_password and self.check_password_format(password):
                self.password = password
                break
            
            else:
                print("최소 8자리(대문자 1개 필수, 문자, 숫자, 특수문자)를 만족하세요.")

        print("계좌 생성")

    def createAccount(self):
        import random
        import string

        length = 8
        string_pool = string.digits
        result = ""

        for i in range(length) :
            # 랜덤한 하나의 숫자를 뽑아서, 문자열 결합을 한다.
            result += random.choice(string_pool)

        self.account = int(result)

    def check_id_format(self, id):
        # 영어, 숫자, 최소 6자리
        if not re.match("^[a-zA-Z0-9]{6,}$", id):
            return False
        return True
    
    def check_exist_id(self):
        return 1

    def check_password_format(self, password):
        # 최소 8자리 (대문자 1개 필수, 문자, 숫자, 특수문자 조합)
        if not re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&#^])[A-Za-z\d@$!%*?&#^]{8,}$", password):
            return False
        return True
    
    def get_user(self):
        return self.id, self.password, self.account, self.deposit
    
    def deleteUser(self):
        id_del = input("삭제할 id를 입력하세요: ")
        password_del = input("삭제할 password를 입력하세요: ")
        return id_del, password_del

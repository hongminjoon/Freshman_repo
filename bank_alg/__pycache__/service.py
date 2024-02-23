import random
import string
from log_data import *
import re


class One :
    def __init__(self):
        self.id = ""
        self.pw = ""
        self.ac = ""
        self.charge = ""
        
    def create_id(self):
        id = input("사용할 ID를 입력해주세요 : ")
        self.id = id
        temp =0
        bool_check = True
        log_check = True
        while temp <3:
            for str in id:
                ascii = ord(str)
                if (ascii >=65 and ascii<=122) or (ascii >=48 and ascii<=57):
                    continue
                else:
                    bool_check = False
                    break
            with open('user_data.log','r') as f :
                for line in f:
                    if 'User ID' in line:
                        match = re.search(r'User ID: ([^,]+)',line)
                        if match :
                            log_id = match.group(1)
                            if log_id == self.id:
                                log_check = False
                
            if any(elem.isdigit() for elem in id) and any(elem.isalpha() for elem in id) and len(id)>=4 and bool_check and log_check: 
                return True
            else :
                if(bool_check != True):
                    print("숫자와 영문으로만 조합하여 ID를 생성해주세요.")
                elif any(elem.isdigit() for elem in id)!=True:
                    print("숫자도 함께 조합하여 ID를 생성해주세요.")
                elif any(elem.isalpha() for elem in id) != True:
                    print("영문도 함께 조합하여 ID를 생성해주세요.")
                elif len(id)<4:
                    print("최소 4자리 이상 기입하여 ID를 생성해주세요.")
                else :
                    print("다른 ID와 일치합니다. 다른 ID를 입력해주세요.")

            temp = temp+1
                
            if temp == 3 :
                return False
            id = input("사용할 ID를 다시 입력해주세요 : ")
                    

    def create_pw(self):
        pw = input("사용할 PW를 입력해주세요 : ")
        self.pw = pw
        temp =0
        bool_check = True
        while temp <3:
            check_upper = any(elem.isupper() for elem in pw)
            check_alpha = any(elem.isalpha() for elem in pw)
            check_isdigit = any(elem.isdigit() for elem in pw)
            check_special = any(elem in pw for elem in "~!@#$%^&*")
        
            for str in pw:
                ascii = ord(str)
            if check_upper and check_alpha and check_isdigit and check_special and bool_check and len(pw)>=8: 
                return True
            else :
                if check_isdigit==False:
                    print("숫자도 함께 조합하여 PW를 생성해주세요.")
                elif check_alpha==False:
                    print("영문도 함께 조합하여 PW를 생성해주세요.")
                elif check_special==False:
                    print("특수문자도 함께 조합하여 PW를 생성해주세요.")
                elif len(pw)<8:
                    print("최소 8자리 이상 기입하여 PW를 생성해주세요.")
                else :
                    print("대문자도 함께 조합하여 PW를 생성해주세요.")
            temp = temp+1
            
                
            if temp == 3 :
                print("3회 이상 잘못 입력하여 ID부터 다시 생성해야합니다.")
                return False
            pw = input("사용할 PW를 다시 입력해주세요 : ")
                    
            
    
    def create_ac(self):
        n = 8
        for i in range(n):
            self.ac += str(random.choice(string.digits)) 
        return 
        
    
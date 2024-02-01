import os
from log import Log

user_list = []

def loading_user_list():
    global user_list
    log = Log()
    log_file_path = "./log/user_log.txt"
    if os.path.exists(log_file_path):
        user_list = log.read_user_log(log_file_path)

def append_user_list(id, password, account, deposit):
    user_list.append({"id":id, "password":password, "account":account, "deposit":deposit})

def delete_user(id_del, password_del):
    global user_list
    login_dict = {user['id']: user['password'] for user in user_list}

    if id_del in login_dict and password_del != login_dict[id_del]:
        print("입력하신 id의 비밀번호가 일치하지 않습니다.")
    elif id_del not in login_dict:
        print("입력하신 id가 존재하지 않습니다.")
    else:
        user_list = [
            {
                "id":user['id'], 
                "password":user['password'], 
                "account":int(user['account']), 
                "deposit":int(user['deposit'])
            } 
            for user in user_list 
            if user['id'] != id_del or user['password'] != password_del
        ]
        print("정상적으로 삭제되었습니다. ")

def get_user_list():
    return user_list

def print_user_list():
    for i in user_list:
        print(i)
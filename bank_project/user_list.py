import os
from log import Log

user_list = []

def loading_user_list():
    global user_list
    log = Log()
    log_file_path = "./log/user_log.txt"
    if os.path.exists(log_file_path):
        user_list = log.read_log(log_file_path)

def append_user_list(id, password, account, deposit):
    user_list.append((id, password, account, deposit))

def delete_user(id_del, password_del):
    global user_list
    login_dict = {username: password for username, password, _, _ in user_list}

    if id_del in login_dict and password_del != login_dict[id_del]:
        print("입력하신 id의 비밀번호가 일치하지 않습니다.")
    elif id_del not in login_dict:
        print("입력하신 id가 존재하지 않습니다.")
    else:
        user_list = [(username, password, account, deposit) for username, password, account, deposit in user_list
                 if username != id_del or password != password_del]
        print("정상적으로 삭제되었습니다. ")

def get_user_list():
    return user_list

def print_user_list():
    for i in user_list:
        print(i)
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


def get_user_list():
    return user_list

def print_user_list():
    for i in user_list:
        print(i)
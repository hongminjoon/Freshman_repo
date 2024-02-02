import random
import os
import user_list
from log import Log

# account : history
# bank_dic = {"111111":[{"receiver_id":"geun4715", "receiver_account":333333,"money":1000000},
#                      {"receiver_id":"geun8881", "receiver_account":222222,"money":1000}]}
bank_dic = {}


class Bank_System:   
    def loading_user_list(self):
        global bank_dic
        log = Log()
        log_file_path = "./log/bank_log.txt"
        if os.path.exists(log_file_path):
            bank_dic = log.read_bank_log(log_file_path)

    def transfer_money(self):
        users = user_list.get_user_list()

        sender = random.choice(users)
        receiver = random.choice([user for user in users if user != sender])
        amount = random.randrange(1000, 100000, 1000)
        
        if amount > sender['deposit']:
            print(f"error : {sender['id']} -> {receiver['id']} 이체 오류")
            print(f"송금자의 돈이 {amount-sender['deposit']} 만큼 부족합니다.")
        
        else:
            sender['deposit'] -= amount
            receiver['deposit'] += amount
            self.append_bank_dictionary(sender['account'], receiver['id'], receiver['account'], amount)
            print(f"송금 기록- 송신자: {sender['id']}, 수신자: {receiver['id']}, 이체금액: {amount}")

    def append_bank_dictionary(self, send_account, receiver_id, receiver_account, money):
        send_account = str(send_account)
        if send_account in bank_dic:
            bank_dic[send_account].append({"receiver_id":receiver_id, "receiver_account":receiver_account,"money":money})
        else:
            bank_dic[send_account] = [{"receiver_id":receiver_id, "receiver_account":receiver_account,"money":money}]
        
    def get_account_history(self, account):
        if account not in bank_dic:
            print(f"계좌번호 '{account}'에 대한 기록이 존재하지 않습니다. ")
        else:
            return bank_dic[account]

    def get_bank_dic(self):
        return bank_dic
    
    def delete_bank(self, del_account):
        del_account = str(del_account)
        if del_account in bank_dic:
            del bank_dic[del_account]

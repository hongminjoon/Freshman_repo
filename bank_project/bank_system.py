import user_list
import random

class Bank_System:   
    
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
            
            print(f"송금 기록- 송신자: {sender['id']}, 수신자: {receiver['id']}, 이체금액: {amount}")
            




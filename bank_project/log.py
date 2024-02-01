from datetime import datetime

class Log:
    
    def save_log(self, user_list):        
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("./log/user_log.txt", "w") as log_file:
            log_file.write(f"{start_time}\n")
            for user in user_list:
                log_file.write(f"{user['id']}, {user['password']}, {user['account']}, {user['deposit']}\n")
    
    def read_log(self, file_path):
        log_data = []
        with open(file_path, "r") as log_file:
            next(log_file)
            for line in log_file:
                entry_parts = line.split(",")
                
                id, password, account, deposit = map(str.strip, entry_parts)
                log_data.append({"id":id, "password":password, "account":account, "deposit":deposit})

        return log_data

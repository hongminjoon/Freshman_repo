# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    dic = {friend:index for index, friend in enumerate(friends)}
    table = [ [0] * len(friends) for _ in range(len(friends))]

    for gift in gifts:
        give, get = gift.split()
        table[dic[give]][dic[get]] += 1
    

    num_gift = {friend: [0, 0] for friend in friends}
    
    for gift in gifts:
        send_friend, get_friend = gift.split()
        num_gift[send_friend][0] += 1
        num_gift[get_friend][1] += 1
    
    gift_jisu = []
    for i in num_gift.values():
        gift_jisu.append(i[0]- i[1])

    answer = [0] * len(friends)
    
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if table[i][j] > table[j][i]:  # 준게 많음
                answer[i] += 1
            elif table[i][j] < table[j][i]: # 받은게 많음
                answer[j] += 1
            else: #없거나 같을때
                if gift_jisu[i] > gift_jisu[j]:
                    answer[i] += 1
                elif gift_jisu[j] > gift_jisu[i]:
                    answer[j] += 1

    return max(answer)

print(solution(["a", "b", "c"],["a b", "b a", "c a", "a c", "a c", "c a"]))

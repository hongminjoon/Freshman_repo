def solution(names, yearnings, photos):
    answer = []
    
    info = dict(zip(names,yearnings))
    for photo in photos:
        count = 0
        for person in photo:
            if person in info:
                count += info[person]
            else:
                continue
        answer.append(count)    

    return answer

print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
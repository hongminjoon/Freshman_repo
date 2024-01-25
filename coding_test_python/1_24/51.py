# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goals):
    card1_index = 0
    card2_index = 0
    for goal in goals:

        if len(cards1) > card1_index and goal == cards1[card1_index]:
            card1_index += 1
        elif len(cards2) > card2_index and goal == cards2[card2_index]:
            card2_index += 1
        else:
            return "No"

    return "Yes"

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
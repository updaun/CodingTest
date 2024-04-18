# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 카드 뭉치
# https://school.programmers.co.kr/learn/courses/30/lessons/159994


from collections import deque

def solution(cards1, cards2, goal):
    d1 = deque(cards1)
    d2 = deque(cards2)
    g = deque(goal)
    d1_temp = []
    d2_temp = []
    for i in goal:
        if len(d1_temp) == 0 and len(d1) != 0:
            d1_temp.append(d1.popleft())
        if len(d2_temp) == 0 and len(d2) != 0:
            d2_temp.append(d2.popleft())
            
        if i not in d1_temp and i not in d2_temp:
            return "No"
        else:
            if i in d1_temp:
                d1_temp.pop()
            if i in d2_temp:
                d2_temp.pop()
    return "Yes"

# 다른 사람의 풀이 (맨 앞만 확인하고 popleft)
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.popleft()      
        elif len(cards2) >0 and g == cards2[0]:
            cards2.popleft()
        else:
            return "No"
    return "Yes"


q = solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"])
assert q == "Yes", "불일치"
print(q)

q = solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"])
assert q == "No", "불일치"
print(q)
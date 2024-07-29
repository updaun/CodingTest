# 프로그래머스
# 코딩테스트 연습 > 탐욕법(Greedy) > 구명보트

# 내 풀이 : 효율성이 많이 떨어짐
# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
#     while people:
#         person = people.pop()
#         for i in range(len(people)):
#             if person + people[i] <= limit:
#                 people.pop(i)
#                 break
#         answer += 1
#     return answer

# Deque를 안 쓰고 풀이
# pop(n)은 o(n)의 시간복잡도를 가지며, pop()은 o(1)의 시간복잡도를 갖는다.
# 그러므로 deque를 사용하여 popleft()까지 사용해야 시간복잡도를 줄일 수 있다.
# def solution(people, limit):
#     answer = 0
#     people.sort()
#     while people:
#         if len(people) == 1:
#             answer += 1
#             break
#         if people[0] + people[-1] <= limit:
#             people.pop(0)
#             people.pop()
#         else:
#             people.pop()
#         answer += 1
#     return answer

from collections import deque
def solution(people, limit):
    answer = 0
    q = deque(sorted(people))
    while q:
        if len(q) == 1:
            answer += 1
            break
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
        else:
            q.pop()
        answer += 1
    return answer

print(solution([70, 50, 80, 50], 100)) # 3
print(solution([70, 80, 50], 100)) # 3
print(solution([30, 40, 50, 60], 100)) # 2
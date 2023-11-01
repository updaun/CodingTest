# 프로그래머스
# 프로그래밍 강의 > PCCP 모의고사 2회 > [PCCP 모의고사 2] 2번
# https://school.programmers.co.kr/learn/courses/15009/lessons/121688

# 시간초과
def solution(ability, number):
    for i in range(number):
        ability.sort()
        a, b = ability[0], ability[1]
        ability[0], ability[1] = a+b, a+b
    return sum(ability)


import heapq
def solution(ability, number):
    heapq.heapify(ability)
    for i in range(number):
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)
        heapq.heappush(ability, a+b)
        heapq.heappush(ability, a+b)
    return sum(ability)

q = solution([10, 3, 7, 2], 2)
assert q == 37, "불일치"
print(q)

q = solution([1, 2, 3, 4], 3)
assert q == 26, "불일치"
print(q)

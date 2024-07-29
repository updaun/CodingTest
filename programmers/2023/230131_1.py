# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 야근 지수

import heapq
def solution(n, works):
    answer = 0
    if sum(works) <= n : return 0
    h = []
    for i in works:
        heapq.heappush(h, -i)
    while n:
        max_work = heapq.heappop(h) + 1
        heapq.heappush(h, max_work)
        n -= 1
    return sum([i**2 for i in h])

print(solution([4, 3, 3], 4)) # 12
print(solution([2, 1, 2], 1)) # 6
print(solution([1,1], 3)) # 0
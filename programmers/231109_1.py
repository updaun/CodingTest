# 프로그래머스
# 프로그래밍 강의 > PCCP 모의고사 2회 > [PCCP 모의고사 2] 3번
# https://school.programmers.co.kr/learn/courses/15009/lessons/121689


# 나의 풀이 시간초과
def solution(menu, order, k):
    answer = 0
    times = []
    leave_time = 0
    for i, drink in enumerate(order):
        arrive_time = i*k
        leave_time += menu[drink]
        times.append((arrive_time, leave_time))
            
    for s in range(times[-1][1]):
        current = 0
        for time in times:
            if time[0] <= s < time[1]:
                current += 1
        answer = max(answer, current)
    
    return answer


# 다른 사람의 풀이(힙을 활용한 풀이)
import heapq

def solution(menu, order, k):
    answer = 1
    start, end = -k, 0
    q = []
    for i in order:
        start += k
        end = max(start, end) + menu[i]
        heapq.heappush(q, end)
        while q:
            now = heapq.heappop(q)
            if start < now:
                heapq.heappush(q, now)
                break
        answer = max(answer, len(q))
    return answer


q = solution([5, 12, 30], [1, 2, 0, 1], 10)
assert q == 3, "불일치"
print(q)

q = solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10)
assert q == 4, "불일치"
print(q)

q = solution([5], [0, 0, 0, 0, 0], 5)
assert q == 1, "불일치"
print(q)


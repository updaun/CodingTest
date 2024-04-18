# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 명예의 전당 (1)

import heapq
def solution(k, score):
    answer = []
    h = []
    for i in score:
        heapq.heappush(h, i)
        if len(answer) >= k:
            heapq.heappop(h)
        answer.append(h[0])
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200])) # [10, 10, 10, 20, 20, 100, 100]
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])) # [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]

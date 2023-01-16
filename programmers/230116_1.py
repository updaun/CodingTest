# 프로그래머스
# 코딩테스트 연습 > 스택/큐 > 프린터

from collections import deque
def solution(priorities, location):
    answer = 0
    printer = deque([(i,p) for i,p in enumerate(priorities)])
    while printer:
        select = printer.popleft()
        if len(printer) == 0:
            return answer + 1
        if select[1] < max([i[1] for i in printer]):
        # if any(select[1] < other[1] for other in printer):
            printer.append(select)
        else:
            answer += 1
            if select[0] == location:
                break
    return answer

print(solution([2, 1, 3, 2], 2)) # 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # 5
print(solution([2, 1, 3, 2], 0)) # 3
print(solution([2], 0)) # 1
# 프로그래머스
# 코딩테스트 연습 > 힙(Heap) > 이중우선순위큐

from collections import deque
def solution(operations):
    q = deque([])
    for case in operations:
        c, num = case.split(" ")
        if c == "I":
            q.append(int(num))
            q = deque(sorted(q))
        else:
            if num == "1" and len(q) != 0:
                q.pop()
            elif num == "-1" and len(q) != 0:
                q.popleft()
    if len(q) != 0:
        return [max(q), min(q)]
    return [0,0]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333, -45]

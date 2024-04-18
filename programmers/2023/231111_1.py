# 프로그래머스
# 프로그래밍 강의 > PCCP 기출문제 > PCCP 기출 1번
# https://school.programmers.co.kr/learn/courses/19344/lessons/242258

from collections import deque
def solution(bandage, health, attacks):
    answer = health
    combo = 0
    play = attacks[-1][0]
    q = deque(attacks)
    c, h, b = bandage
    for s in range(1, play+1):
        combo += 1
        if s == q[0][0]:
            attack = q.popleft()
            combo = 0
            answer -= attack[1]
            if answer <= 0:
                return -1
        else:
            if answer < health:
                answer += h
                if combo == c:
                    answer += b
                    combo = 0
                if answer > health:
                    answer = health
    return answer


q = solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])
assert q == 5, "불일치"
print(q)

q = solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
assert q == -1, "불일치"
print(q)

q = solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
assert q == -1, "불일치"
print(q)

q = solution([1, 1, 1], 5, [[1, 2], [3, 2]])
assert q == 3, "불일치"
print(q)

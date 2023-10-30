# 프로그래머스
# 프로그래밍 강의 > PCCP 모의고사 2회 > [PCCP 모의고사 2] 1번
# https://school.programmers.co.kr/learn/courses/15009/lessons/121687

from collections import deque
def solution(command):
    answer = [0, 0]
    case = [[[0, 1], [0, -1]], [[1, 0], [-1, 0]], [[0, -1], [0, 1]], [[-1, 0], [1, 0]]]
    directions = deque(case)
    for s in command:
        if s == "G":
            x, y = directions[0][0]
            answer[0] += x
            answer[1] += y
        elif s == "B":
            x, y = directions[0][1]
            answer[0] += x
            answer[1] += y
        elif s == "R":
            directions.rotate(-1)
        elif s == "L":
            directions.rotate(1)
    return answer

q = solution("GRGLGRG")
assert q == [2, 2], "불일치"
print(q)

q = solution("GRGRGRB")
assert q == [2, 0], "불일치"
print(q)
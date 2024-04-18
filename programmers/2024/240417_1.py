# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 택배상자
# https://school.programmers.co.kr/learn/courses/30/lessons/131704?language=python3

from collections import deque

def solution(order):
    answer = []
    origin = deque(range(1, len(order)+1))
    stack = []
    temp = 0
    for i in order:
        temp += 1
        if stack and stack[-1] == i:
            answer.append(stack.pop())
        if origin and origin[0] == i:
            answer.append(origin.popleft())

        while origin and origin[0] != i:
            stack.append(origin.popleft())
        else:
            if origin:
                answer.append(origin.popleft())

        if temp > len(answer):
            break

    return len(answer)

q = solution([4, 3, 1, 2, 5])
assert q == 2, "불일치"
print(q)

q = solution([5, 4, 3, 2, 1])
assert q == 5, "불일치"
print(q)

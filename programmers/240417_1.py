# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 택배상자
# https://school.programmers.co.kr/learn/courses/30/lessons/131704?language=python3

from collections import deque

def solution(order):
    answer = []
    origin = deque(list(range(1, len(order)+1)))
    stack = []
    for i in order:
        if stack and stack[-1] == i:
            answer.append(stack.pop())
        if origin and stack and i != origin[0] and i != stack[-1]:
            break
        while origin:
            temp = origin.popleft()
            if temp != i:
                stack.append(temp)
            else:
                answer.append(i)
                break
    return len(answer)

q = solution([4, 3, 1, 2, 5])
assert q == 2, "불일치"
print(q)

q = solution([5, 4, 3, 2, 1])
assert q == 5, "불일치"
print(q)

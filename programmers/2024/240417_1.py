# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 택배상자
# https://school.programmers.co.kr/learn/courses/30/lessons/131704?language=python3

def solution(order):
    answer = 0
    i = 1
    stack = []

    while i != len(order) + 1:
        stack.append(i)
        while stack[-1] == order[answer]:
            answer += 1
            stack.pop()
            if len(stack) == 0:
                break
        i += 1
    return answer

q = solution([4, 3, 1, 2, 5])
assert q == 2, "불일치"
print(q)

q = solution([5, 4, 3, 2, 1])
assert q == 5, "불일치"
print(q)

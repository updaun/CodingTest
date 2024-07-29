# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 간단한 논리 연산
# https://school.programmers.co.kr/learn/courses/30/lessons/181917


def solution(arr):
    temp = 1
    l = len(arr)
    while temp < l:
        temp *= 2
    return arr + [0] * (temp - l)


q = solution([1, 2, 3, 4, 5, 6])
assert q == [1, 2, 3, 4, 5, 6, 0, 0], "불일치"
print(q)

q = solution([58, 172, 746, 89])
assert q == [58, 172, 746, 89], "불일치"
print(q)
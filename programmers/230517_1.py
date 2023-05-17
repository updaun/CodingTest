# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 조건에 맞게 수열 변환하기 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181835


def solution(arr, k):
    return list(map(lambda x: x*k, arr)) if k % 2 == 1 else list(map(lambda x: x+k, arr))

q = solution([1, 2, 3, 100, 99, 98], 3)
assert q == [3, 6, 9, 300, 297, 294], "불일치"
print(q)

q = solution([1, 2, 3, 100, 99, 98], 2)
assert q == [3, 4, 5, 102, 101, 100], "불일치"
print(q)
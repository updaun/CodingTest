# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 조건에 맞게 수열 변환하기 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181882


def solution(arr):
    return [i//2 if i >= 50 and i % 2 == 0 else i*2 if i < 50 and i % 2 == 1 else i for i in arr]

q = solution([1, 2, 3, 100, 99, 98])
assert q == [2, 2, 6, 50, 99, 49], "불일치"
print(q)
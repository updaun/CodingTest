# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181856?language=python3


def solution(arr1, arr2):
    len_a = len(arr1)
    len_b = len(arr2)
    if len_a == len_b:
        a = sum(arr1)
        b = sum(arr2)
        if a==b: return 0
        if a>b: return 1
        return -1
    else:
        if len_a > len_b: return 1
        return -1

q = solution([49, 13], [70, 11, 2])
assert q == -1, "불일치"
print(q)

q = solution([100, 17, 84, 1], [55, 12, 65, 36])
assert q == 1, "불일치"
print(q)

q = solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3])
assert q == 0, "불일치"
print(q)


# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 특별한 이차원 배열 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181831


def solution(arr):
    l = len(arr[0])
    for i in range(len(arr)):
        for j in range(l):
            if i != j and arr[i][j] != arr[j][i]:
                return 0
    return 1


q = solution([[5, 192, 33], [192, 72, 95], [33, 95, 999]])
assert q == 1, "불일치"
print(q)

q = solution([[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]])
assert q == 0, "불일치"
print(q)

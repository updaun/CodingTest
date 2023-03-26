# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 땅따먹기
# https://school.programmers.co.kr/learn/courses/30/lessons/12913


def solution(land):
    for row_i, row in enumerate(land[:-1]):
        for i in range(len(row)):
            copy = row.copy()
            copy.pop(i)
            land[row_i+1][i] += max(copy)
    return max(land[-1])


q = solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])
assert q == 16, "불일치"
print(q)

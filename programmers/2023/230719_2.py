# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 등차수열의 특정한 항만 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181931


def solution(a, d, included):
    return sum([v for i, v in enumerate(list(range(a,a+d*len(included), d))) if included[i]])


q = solution(3, 4, [True, False, False, True, True])
assert q == 37, "불일치"
print(q)

q = solution(7, 1, [False, False, False, True, False, False, False]	)
assert q == 10, "불일치"
print(q)

# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 배열 만들기 5
# https://school.programmers.co.kr/learn/courses/30/lessons/181931


def solution(intStrs, k, s, l):
    return [int(i[s:s+l]) for i in intStrs if int(i[s:s+l]) > k]


q = solution(["0123456789","9876543210","9999999999999"], 50000, 5, 5)
assert q == [56789, 99999], "불일치"
print(q)

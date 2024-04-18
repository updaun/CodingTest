# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > x 사이의 개수
# https://school.programmers.co.kr/learn/courses/30/lessons/181867


def solution(myString):
    return [len(i) for i in myString.split("x")]

q = solution("oxooxoxxox")
assert q == [1, 2, 1, 0, 1, 0], "불일치"
print(q)

q = solution("xabcxdefxghi")
assert q == [0, 3, 3, 3], "불일치"
print(q)

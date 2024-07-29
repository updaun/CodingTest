# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 간단한 식 계산하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181865


def solution(binomial):
    a, m, b = [int(i) if i.isdigit() else i for i in binomial.split()]
    if m == "+": return a+b
    elif m == "-": return a-b
    else: return a*b

q = solution("43 + 12")
assert q == 55, "불일치"
print(q)

q = solution("0 - 7777")
assert q == -7777, "불일치"
print(q)

q = solution("40000 * 40000")
assert q == 1600000000, "불일치"
print(q)

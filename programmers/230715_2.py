# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 주사위 게임 2
# https://school.programmers.co.kr/learn/courses/30/lessons/181930


def solution(a, b, c):
    d = set([a, b, c])
    if len(d) == 1:
        return 3**3 * a * a**2 * a**3
    elif len(d) == 2:
        return (a+b+c) * (a**2+b**2+c**2)
    else:
        return a+b+c


q = solution(2,6,1)
assert q == 9, "불일치"
print(q)

q = solution(5,3,3)
assert q == 473, "불일치"
print(q)

q = solution(4,4,4)
assert q == 110592, "불일치"
print(q)
# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 주사위 게임 3
# https://school.programmers.co.kr/learn/courses/30/lessons/181916

from collections import Counter
def solution(a, b, c, d):
    dice = Counter([a,b,c,d])
    sorted_dice = sorted(dice, key=lambda x:dice[x])
    temp = max(dice.values())
    keys = list(dice.keys())
    if temp == 4:
        return 1111*keys[0]
    if temp == 3:
        q, p = sorted_dice
        return (10*p+q)**2
    if temp == 2:
        if len(keys) == 3:
            q, r, p = sorted_dice
            return q*r
        else:
            p, q = keys
            return (p+q)*abs(p-q)
    if temp == 1:
        return min(keys)



q = solution(2, 2, 2, 2)
assert q == 2222, "불일치"
print(q)

q = solution(4, 1, 4, 4)
assert q == 1681, "불일치"
print(q)

q = solution(6, 3, 3, 6)
assert q == 27, "불일치"
print(q)

q = solution(2, 5, 2, 6)
assert q == 30, "불일치"
print(q)

q = solution(6, 4, 2, 5)
assert q == 2, "불일치"
print(q)

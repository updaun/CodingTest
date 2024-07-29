# 프로그래머스
# 프로그래밍 강의 > PCCP 모의고사 1회 > [PCCP 모의고사 1] 2번
# https://school.programmers.co.kr/learn/courses/15008/lessons/121683

from itertools import permutations
def solution(ability):
    answer = 0
    n, m = len(ability), len(ability[0])
    indexs = list(range(n))
    for com in permutations(indexs, m):
        temp = [ability[v][i] for i, v in enumerate(com)]
        sum_temp = sum(temp)
        answer = max(answer, sum_temp)
    return answer

q = solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]])
assert q == 210, "불일치"
print(q)

q = solution([[20, 30], [30, 20], [20, 30]]	)
assert q == 60, "불일치"
print(q)


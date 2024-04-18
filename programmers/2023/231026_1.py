# 프로그래머스
# 프로그래밍 강의 > PCCP 모의고사 1회 > [PCCP 모의고사 1] 3번
# https://school.programmers.co.kr/learn/courses/15008/lessons/121685


def bean(generation, order):
    if generation == 1: return "Rr"
    
    parent = bean(generation - 1, (order -1) // 4 + 1 )
    if parent == "RR" or parent == "rr": return parent

    if order % 4 == 0:
        return "rr"
    elif order % 4 == 1:
        return "RR"
    else:
        return "Rr"

def solution(queries):
    answer = []
    for query in queries:
        n, p = query
        answer.append(bean(n, p))
    return answer

q = solution([[3, 5]])
assert q == ["RR"], "불일치"
print(q)

q = solution([[3, 8], [2, 2]])
assert q == ["rr", "Rr"], "불일치"
print(q)

q = solution([[3, 1], [2, 3], [3, 9]])
assert q == ["RR", "Rr", "RR"], "불일치"
print(q)

q = solution([[4, 26]])
assert q == ["Rr"], "불일치"
print(q)
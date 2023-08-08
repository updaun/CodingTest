# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 전국 대회 선발 고사
# https://school.programmers.co.kr/learn/courses/30/lessons/181851

def solution(rank, attendance):
    attend = [(rank[i], i) for i, v in enumerate(attendance) if v]
    a,b,c = sorted(attend)[:3]
    return 10000*a[1] + 100*b[1] + c[1]

q = solution([3, 7, 2, 5, 4, 6, 1], [False, True, True, True, True, False, False])
assert q == 20403, "불일치"
print(q)

q = solution([1, 2, 3], [True, True, True])
assert q == 102, "불일치"
print(q)

q = solution([6, 1, 5, 2, 3, 4], [True, False, True, False, False, True])
assert q == 50200, "불일치"
print(q)
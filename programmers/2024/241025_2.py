# 프로그래머스
# 코딩테스트 연습 > PCCP 기출문제 > [PCCP 기출문제] 1번 / 붕대 감기
# https://school.programmers.co.kr/learn/courses/30/lessons/250137

def solution(bandage, health, attacks):
    answer = health
    temp = 0
    last_t = 0
    c, h, b = bandage
    for attack in attacks:
        t, d = attack
        temp = t-last_t-1
        last_t = t
        heling = temp * h + (temp//c)*b
        answer += heling     
        answer = min(answer, health)
        answer -= d
        if answer <= 0:
            return -1
    return answer

q = solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])
assert q == 5, f"잘못된 결과: {q}"
print(q)

q = solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
assert q == -1, f"잘못된 결과: {q}"
print(q)

q = solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])
assert q == -1, f"잘못된 결과: {q}"
print(q)

q = solution([1, 1, 1], 5, [[1, 2], [3, 2]])
assert q == 3, f"잘못된 결과: {q}"
print(q)
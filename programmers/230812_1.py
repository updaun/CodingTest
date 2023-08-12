# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 덧칠하기
# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 0
    temp = 0
    for i in section:
        if temp <= i:
            temp = i + m
            answer += 1
    return answer


q = solution(8, 4, [2, 3, 6])
assert q == 2, "불일치"
print(q)

q = solution(5, 4, [1, 3])
assert q == 1, "불일치"
print(q)

q = solution(4, 1, [1, 2, 3, 4])
assert q == 4, "불일치"
print(q)

q = solution(4, 2, [3])
assert q == 1, "불일치"
print(q)

q = solution(5, 2, [1, 4, 5])
assert q == 2, "불일치"
print(q)

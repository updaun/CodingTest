# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 특별한 이차원 배열 1
# https://school.programmers.co.kr/learn/courses/30/lessons/181919


def solution(n):
    answer = []
    for i in range(n):
        answer.append([1 if j==i else 0 for j in range(n)])
    return answer


q = solution(3)
assert q == [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "불일치"
print(q)

q = solution(6)
assert q == [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]], "불일치"
print(q)

q = solution(1)
assert q == [[1]], "불일치"
print(q)

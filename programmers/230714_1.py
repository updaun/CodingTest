# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 두 수의 연산값 비교하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181938


def solution(a, b):
    return max(int(str(a)+str(b)), 2*a*b)


q = solution(2, 91)
assert q == 364, "불일치"
print(q)

q = solution(91, 2)
assert q == 912, "불일치"
print(q)

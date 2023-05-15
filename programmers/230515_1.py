# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 길이에 따른 연산
# https://school.programmers.co.kr/learn/courses/30/lessons/181879

from functools import reduce
import operator

def solution(num_list):
    return sum(num_list) if len(num_list) >= 11  else reduce(operator.mul, num_list, 1)


q = solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1])
assert q == 51, "불일치"
print(q)

q = solution([2, 3, 4, 5])
assert q == 120, "불일치"
print(q)
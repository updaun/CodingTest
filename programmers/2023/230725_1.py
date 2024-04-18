# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 간단한 논리 연산
# https://school.programmers.co.kr/learn/courses/30/lessons/181917


def solution(x1, x2, x3, x4):
    return bool((x1+x2)*(x3+x4))


# 다른 사람의 풀이
def solution(x1, x2, x3, x4):
    return (x1 | x2) & (x3 | x4)

q = solution(False, True, True, True)
assert q == True, "불일치"
print(q)

q = solution(True, False, False, False)
assert q == False, "불일치"
print(q)
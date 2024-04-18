# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 홀짝에 따라 다른 값 반환하기
# https://school.programmers.co.kr/learn/courses/30/lessons/181935


def solution(n):
    return sum([i**2 for i in list(range(2, n+1, 2))]) if n%2==0 else sum(list(range(1,n+1,2)))
    

q = solution(7)
assert q == 16, "불일치"
print(q)

q = solution(10)
assert q == 220, "불일치"
print(q)

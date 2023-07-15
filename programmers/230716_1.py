# 프로그래머스
# 코딩테스트 연습 > 코딩 기초 트레이닝 > 콜라츠 수열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/181919


def solution(n):
    answer = [n]
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3*n+1
        answer.append(n)
    return answer


q = solution(10)
assert q == [10, 5, 16, 8, 4, 2, 1], "불일치"
print(q)

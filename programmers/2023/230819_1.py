# 프로그래머스
# 코딩테스트 연습 > 월간 코드 챌린지 시즌2 > 2개 이하로 다른 비트
# https://school.programmers.co.kr/learn/courses/30/lessons/77885


def solution(numbers):
    answer = []
    for number in numbers:
        now = number
        temp = number
        n = 0
        c = 0
        while temp > 0:
            if temp % 2 == 0:
                break
            temp = temp // 2
            n += 1
        if n == 0:
            c = number + 1
        else:
            c = now + 2**n - 2**(n-1)
        answer.append(c)
    return answer

q = solution([2, 7])
assert q == [3, 11], "불일치"
print(q)

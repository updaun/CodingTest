# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 콜라 문제

def solution(a, b, n):
    answer = 0
    while n >= a:
        m, r = divmod(n, a)
        n = m*b + r
        answer += m*b
    return answer

print(solution(2, 1, 20)) # 19
print(solution(3, 1, 20)) # 9
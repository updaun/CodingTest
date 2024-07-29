# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 최고의 집합

def solution(n, s):
    answer = []
    d, r = divmod(s, n)
    if d == 0:
        return [-1]
    answer = [d]*n
    for i in range(r):
        answer[-(i+1)] += 1
    return answer

print(solution(2, 9)) # [4, 5]
print(solution(2, 1)) # [-1]
print(solution(2, 8)) # [4, 4]
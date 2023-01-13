# 프로그래머스
# 코딩테스트 연습 > 연습문제 > 소수 찾기

def solution(n):
    answer = [False, False] + [True]*(n-1)
    for i in range(2, n+1):
        for j in range(2*i, n+1, i):
            answer[j] = False
    return answer.count(True)

print(solution(10)) # 4
print(solution(5)) # 3
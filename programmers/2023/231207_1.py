# 프로그래머스
# 코딩테스트 연습 > 동적계획법(Dynamic Programming) > 등굣길
# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for i in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue 
            if [j, i] in puddles:    
                dp[i][j] = 0
            else:     
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n][m]

q = solution(4, 3, [[2, 2]])
assert q == 4, "불일치"
print(q)

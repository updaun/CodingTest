import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0]*m for _ in range(n)]
d = []
for i in range(m):
    d.append([int(i) for i in input().rstrip()])

answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = d[i][j]
        elif d[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        answer = max(dp[i][j], answer)

print(answer**2)
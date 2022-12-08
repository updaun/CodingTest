import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = [list(map(int, input().split())) for i in range(n)]
s = [[0]*(m+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        s[i][j] = d[i-1][j-1] + max(s[i-1][j], s[i][j-1], s[i-1][j-1])

print(s[n][m])

# BFS 풀이시 시간초과 발생
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# d = [list(map(int, input().split())) for i in range(n)]
# s = [[0]*m for i in range(n)]
# dx = [0, 1, 1]
# dy = [1, 0, 1]
# q = []
# s[0][0] = d[0][0]

# def bfs(x, y):
#     q.append((x, y))
#     while q:
#         x, y = q.pop(0)
#         for i in range(2):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
                                
#             s[nx][ny] = max(s[nx][ny], s[x][y]+d[nx][ny])
#             q.append((nx, ny))

# bfs(0,0)
# print(s[n-1][m-1])
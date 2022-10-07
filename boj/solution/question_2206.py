import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
d = [list(map(int, [i for i in input().rstrip()])) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1

    while q:
        x, y, w = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][w]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if d[nx][ny] == 0 and visited[nx][ny][w] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                q.append([nx, ny, w])
            elif d[nx][ny] == 1 and w == 0:
                visited[nx][ny][w+1] = visited[x][y][w] + 1
                q.append([nx, ny, w+1])
    
    return -1

print(bfs())

# 시간초과
# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# d = [list(map(int, [i for i in input().rstrip()])) for _ in range(n)]

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]

# def bfs():
#     queue = [(0,0)]

#     while queue:
#         x, y = queue.pop(0)

#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]

#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue

#             if d[nx][ny] == 0:
#                 queue.append((nx, ny))
#                 d[nx][ny] = d[x][y] + 1
    
#     if nx != n-1 and ny != m-1:
#         return -1
#     return d[n-1][m-1] + 1

    
# result = []
# def crash_wall(count):
    
#     if count == 1:
#         result.append(bfs())
#         return

#     for i in range(n):
#         for j in range(m):
#             if d[i][j] == 1:
#                 d[i][j] = 0
#                 crash_wall(count+1)
#                 d[i][j] = 1
# crash_wall(0)
# print(max(result))
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = [(x, y)]
    d[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if d[nx][ny] == 1:
                queue.append((nx, ny))
                d[nx][ny] = 0

t =  int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    d = [[0]*n for i in range(m)]
    cnt = 0
    for i in range(k):
        x, y = map(int, input().split())
        d[x][y] = 1
    for x in range(m):
        for y in range(n):
            if d[x][y] == 1:
                bfs(x, y)
                cnt += 1
    print(cnt)
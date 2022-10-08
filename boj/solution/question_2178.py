import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    d.append([int(i) for i in input().rstrip()])

def bfs(x, y):
    queue = [(x,y)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if d[nx][ny] == 1:
                queue.append((nx, ny))
                d[nx][ny] = d[x][y] + 1
    return d[n-1][m-1]

print(bfs(0, 0))

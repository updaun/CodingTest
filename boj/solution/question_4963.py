import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]

def dfs(x,y):
    
    d[x][y] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if d[nx][ny] == 1:
            dfs(nx, ny)

while True:
    n, m = map(int, input().split())
    result = 0
    if n == 0 and m == 0:
        break

    d = []
    for i in range(m):
        d.append(list(map(int, input().split())))

    for x in range(m):
        for y in range(n):
            if d[x][y] == 1:
                dfs(x, y)
                result += 1
    print(result)

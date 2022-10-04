import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    
    queue = []
    clone_d = copy.deepcopy(d)
    for x in range(n):
        for y in range(m):
            if clone_d[x][y] == 2:
                queue.append((x,y))

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if clone_d[nx][ny] == 0:
                clone_d[nx][ny] = 2
                queue.append((nx, ny))
    global answer
    temp = 0
    for i in range(n):
        temp += clone_d[i].count(0)
    answer = max(answer, temp)


def install_wall(count):
    if count == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if d[i][j] == 0:
                d[i][j] = 1
                install_wall(count+1)
                d[i][j] = 0

answer = 0
install_wall(0)
print(answer)
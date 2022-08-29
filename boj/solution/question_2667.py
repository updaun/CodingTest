# BFS 풀이
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x,y):
    queue = [(x,y)]
    d[x][y] = 0
    count = 1

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if d[nx][ny] == 1:
                queue.append((nx,ny))
                d[nx][ny] = 0
                count += 1
    return count

n = int(input())
d = []
result = 0
count = 0
num = []
for i in range(n):
    d.append([int(i) for i in input().rstrip()])

for x in range(n):
    for y in range(n):
        if d[x][y] == 1:
            num.append(bfs(x, y))
print(len(num))
print("\n".join(map(str, sorted(num))))


# DFS 풀이
import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
d = []
result = 0
count = 0
num = []
for i in range(n):
    d.append([int(i) for i in input().rstrip()])

def dfs(x,y):
    if x < 0 or x>=n or y < 0 or y >= n:
        return False
    if d[x][y] == 1:
        global count
        count += 1
        d[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False

for x in range(n):
    for y in range(n):
        if dfs(x,y) == True:
            num.append(count)
            result += 1
            count = 0
print(result)
print("\n".join(map(str, sorted(num))))

print(d)

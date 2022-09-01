import sys
from pprint import pprint
input =  sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y,d,v):
    v[x][y] = True

    c = d[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0  or nx >= n or ny < 0 or ny >= n:
            continue

        if c == d[nx][ny] and v[nx][ny] == False:
            dfs(nx, ny, d, v)

n = int(input())
d = []
d2 = []
result = 0
result2 = 0
v = [[False]*n for i in range(n)]
v2 = [[False]*n for i in range(n)]
for i in range(n):
    input_c = input().rstrip()
    d.append([c for c in input_c])
    d2.append(["B" if c == 'B' else "G" for c in input_c])

for x in range(n):
    for y in range(n):
        if v[x][y] == False:
            dfs(x,y,d,v)
            result += 1
for x in range(n):
    for y in range(n):
        if v2[x][y] == False:
            dfs(x,y,d2,v2)
            result2 += 1

print(result, result2)
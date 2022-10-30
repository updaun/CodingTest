# 고민하다가 블로그 찾아봄
# https://pacific-ocean.tistory.com/400

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
q = deque()
s = []
visit = [[[0]*64 for i in range(m)] for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y, c, cnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and s[nx][ny] != "#" and visit[nx][ny][c] == 0:
                if s[nx][ny] == ".":
                    visit[nx][ny][c] = 1
                    q.append([nx, ny, c, cnt+1])
                elif s[nx][ny] == "1":
                    return cnt + 1
                else:
                    if s[nx][ny].isupper():
                        if c & 1 << (ord(s[nx][ny])-65):
                            visit[nx][ny][c] = 1
                            q.append([nx, ny, c, cnt+1])
                    elif s[nx][ny].islower():
                        nc = c | 1 << (ord(s[nx][ny])-97)
                        if visit[nx][ny][nc] == 0:
                            visit[nx][ny][nc] = 1
                            q.append([nx, ny, nc, cnt+1])

    return -1

for i in range(n):
    a = list(input().strip())
    s.append(a)
    for j in range(m):
        if a[j] == "0":
            q.append([i, j, 0, 0])
            s[i][j] = "."
            visit[i][j][0] = 1

print(bfs())

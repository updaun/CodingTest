# 2022 Winter Coding - 겨울방학 스타트업 인턴 프로그램
# 다 못 맞춤 부분점수 (55/100)
# [".XX..", ".XX..", ".XX..", ".XX.."]
# 배가 오른쪽을 보고 있다.
# 배의 방향을 관리했어야 했는데, 그렇게 하지 못해 모든 테스트케이스를 통과할 수 없었다.
from collections import deque

def solution(worldmap):

    n, m = len(worldmap), len(worldmap[0])
    f = [list(i) for i in worldmap]
    visited = [[0]*m for i in range(n)]
    q = deque()

    dx = [1, 0, 1, -1]
    dy = [0, 1, 1, 1]

    q.append([0,0,0])

    while q:
        x, y, cnt = q.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and f[nx][ny] == '.':
                if dx[i] == 1 and dy[i] == 1:
                    if f[nx-1][ny] != 'X' and f[nx][ny-1] != 'X':
                        q.append([nx, ny, cnt+1])
                        # print(nx, ny)
                        visited[nx][ny] = 1
                else:
                    q.append([nx, ny, cnt+1])
                    # print(nx, ny)
                    visited[nx][ny] = 1

                if nx == m-1 and ny == n-1:
                    return cnt + 1

    # return answer
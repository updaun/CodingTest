import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = map(int, input().split())
d = []

for i in range(r):
    d.append([i for i in input().rstrip()])

def bfs(d):
    result = 1
    queue = set()
    queue.add((0,0,d[0][0]))

    while queue:
        x, y, road = queue.pop()
        result = max(result, len(road))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            if d[nx][ny] not in road:
                queue.add((nx, ny, road+d[nx][ny]))

    print(result)

bfs(d)

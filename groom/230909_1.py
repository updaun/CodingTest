# 구름LEVEL
# 뭉친 K
# https://level.goorm.io/exam/177478/%EB%AD%89%EC%B9%9C-k/quiz/1

from collections import deque
n = int(input())
a, b = map(int, input().split())
m = [list(map(int, input().split())) for i in range(n)]
c = m[a-1][b-1]

visited = [[False for _ in range(n)] for _ in range(n)]
areas = []

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(grid, start, target, visited):
	rows, cols = len(grid), len(grid[0])
	
	q = deque([start])
	visited[start[0]][start[1]] = True
	size = 0
	
	while q:
		x, y = q.popleft()
		size += 1
		
		for i in range(4):
			nx, ny = x+dx[i], y+dy[i]
			
			if 0 <= nx < rows and 0 <= ny < cols:
				if not visited[nx][ny] and grid[nx][ny] == target:
					visited[nx][ny] = True
					q.append((nx, ny))
	
	return size
	
for i in range(n):
	for j in range(n):
		if m[i][j] == c and not visited[i][j]:
			areas.append(bfs(m, (i, j), c, visited))
					 
print(max(areas))
	
# 4
# 1 2
# 0 0 1 1
# 0 1 1 0
# 0 0 0 1
# 1 1 1 1

# 6

# 4
# 1 2
# 0 0 1 2
# 2 1 1 2
# 2 0 0 2
# 1 1 1 2

# 2
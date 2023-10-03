# 구름LEVEL
# 발전기
# https://level.goorm.io/exam/195694/%EB%B0%9C%EC%A0%84%EA%B8%B0/quiz/1

n = int(input())
f = [list(map(int, input().split())) for i in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(f, i, j):
	if f[i][j] == 0:
		return 0
	stack =[(i, j)]
	while stack:
		x, y = stack.pop()
		if f[x][y] == 0:
			continue
			
		f[x][y] = 0
		for ix, iy in zip(dx, dy):
			nx, ny = x+ix, y+iy
			if 0 <= nx < n and 0 <= ny < n and f[nx][ny] == 1:
				stack.append((nx, ny))
	
	return 1
	
count = 0
	
for i in range(n):
	for j in range(n):
		if f[i][j] == 1:
			count += bfs(f, i, j)
print(count)

# 3
# 0 1 0
# 1 0 1
# 1 1 1

# 2

# 4
# 1 1 1 1
# 0 0 0 1
# 1 1 1 1
# 1 0 0 1

# 3
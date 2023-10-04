# 구름LEVEL
# 발전기 (2)
# https://level.goorm.io/exam/195695/%EB%B0%9C%EC%A0%84%EA%B8%B0-2/quiz/1

n, k = map(int, input().split())
f = [list(map(int, input().split())) for i in range(n)]
count = [0]*31
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(i, j):
	
	stack = [(i, j)]
	M = f[i][j]
	cnt = 0
	while stack:
		x, y = stack.pop()
		if f[x][y] != M:
			continue
		
		f[x][y] = 0
		cnt += 1
		for ix, iy in zip(dx, dy):
			nx, ny = x+ix, y+iy
			if 0 <= nx < n and 0 <= ny < n and f[nx][ny] == M:
				stack.append((nx, ny))
	return cnt

for i in range(n):
	for j in range(n):
		if f[i][j]:
			M = f[i][j]
			if bfs(i,j) >= k:
				count[M] += 1
	
result, temp = 0, 0
for i in range(31):
	if temp <= count[i]:
		result = i
		temp = count[i]
print(result)
			

# 3 2
# 1 1 3
# 2 2 3
# 3 3 2

# 3

# 5 3
# 1 1 1 2 2
# 3 3 3 1 2
# 1 1 2 1 1
# 1 2 2 2 2
# 3 1 1 1 1

# 1
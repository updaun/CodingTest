# 구름LEVEL
# 구름 찾기 깃발
# https://level.goorm.io/exam/195689/%EA%B5%AC%EB%A6%84-%EC%B0%BE%EA%B8%B0-%EA%B9%83%EB%B0%9C/quiz/1

n, k = map(int, input().split())
f = [list(map(int, input().split())) for _ in range(n)]

def check(i, j):
	dx = [1, 1, 1, 0, 0, 0, -1, -1, -1]
	dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]
	c = 0
	for x,y in zip(dx, dy):
		nx, ny = i+x, j+y
		if 0 <= nx < n and 0 <= ny < n:
			if f[nx][ny] == 1:
				c += 1
	return c

result = 0
for i in range(n):
	for j in range(n):
		g = f[i][j]
		if g == 0:
			s = check(i,j)	
			if s == k:
				result += 1
				
print(result)
		
# 4 2
# 0 0 0 1
# 0 0 1 0
# 0 0 1 0
# 0 1 1 1

# 2

# 5 8
# 0 1 1 1 1
# 0 1 0 1 0
# 0 1 1 1 1
# 0 1 1 0 1
# 0 1 0 1 0

# 1
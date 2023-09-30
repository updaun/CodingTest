# 구름LEVEL
# 폭탄 구현하기 (2)
# https://level.goorm.io/exam/195691/%ED%8F%AD%ED%83%84-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-2/quiz/1

# 시간초과
n, k = map(int, input().split())
m = [input().split(" ") for i in range(n)]
booms = [tuple(map(int, input().split())) for i in range(k)]
dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]
f = [[0]*n for i in range(n)]
d = []
c = []
for i in range(n):
	for j in range(n):
		if m[i][j] == "@":
			d.append((i+1, j+1))
		elif m[i][j] == "#":
			c.append((i+1, j+1))
			
for y, x in booms:
	for iy, ix in zip(dy, dx): 
		ny = y+iy
		nx = x+ix
		if 0 <= nx <= n and 0 <= ny <= n:
			if (ny, nx) in d:
				f[ny-1][nx-1] += 2
			elif (ny, nx) in c:
				pass
			else:
				f[ny-1][nx-1] += 1
print(max([max(i) for i in f]))

# 개선사항
# 1. d, c를 set으로 변경
# 2. if 0 <= nx <= n and 0 <= ny <= n: -> if 0 < nx <= n and 0 < ny <= n:
# 3. max([max(i) for i in f]) -> max(map(max, f))

n, k = map(int, input().split())
m = [input().split(" ") for i in range(n)]
booms = [tuple(map(int, input().split())) for i in range(k)]
dx = [0, -1, 0, 1, 0]
dy = [0, 0, -1, 0, 1]
f = [[0]*n for i in range(n)]
d = set()
c = set()
for i in range(n):
	for j in range(n):
		if m[i][j] == "@":
			d.add((i+1, j+1))
		elif m[i][j] == "#":
			c.add((i+1, j+1))
			
for y, x in booms:
	for iy, ix in zip(dy, dx): 
		ny = y+iy
		nx = x+ix
		if 0 < nx <= n and 0 < ny <= n:
			if (ny, nx) in d:
				f[ny-1][nx-1] += 2
			elif (ny, nx) not in c:
				f[ny-1][nx-1] += 1
				
print(max(map(max, f)))
	
# 4 4
# 0 0 @ 0
# 0 0 0 0
# 0 # 0 0
# 0 0 0 @
# 2 2
# 2 3
# 1 4
# 1 4

# 6

# 4 4
# 0 @ 0 0
# @ 0 @ 0
# 0 @ 0 0
# 0 0 0 0
# 2 2
# 2 2
# 2 2
# 2 2

# 8
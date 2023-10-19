# 구름LEVEL
# 중첩 점
# https://level.goorm.io/exam/195700/%EC%A4%91%EC%B2%A9-%EC%A0%90/quiz/1

N, M = map(int, input().split())
arr = [[[0, 0] for _ in range(N)] for i in range(N)]

for _ in range(M):
	y, x, d = input().split()
	y = int(y) - 1
	x = int(x) - 1
	
	if d == "R":
		for j in range(x, N):
			arr[y][j][1] += 1
	elif d == "L":
		for j in range(x+1):
			arr[y][j][1] += 1
	elif d == "U":
		for i in range(y+1):
			arr[i][x][0] += 1
	elif d == "D":
		for i in range(y, N):
			arr[i][x][0] += 1

result = 0
for i in range(N):
	for j in range(N):
		result += arr[i][j][0] * arr[i][j][1]
	
print(result)

# 3 5
# 2 1 R
# 1 1 D
# 2 3 L
# 3 3 U
# 2 2 D

# 6


# 3 3
# 2 2 R
# 2 2 L
# 1 2 D

# 2
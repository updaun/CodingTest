# 구름LEVEL
# 개미 집합의 지름
# https://level.goorm.io/exam/49060/%EA%B0%9C%EB%AF%B8-%EC%A7%91%ED%95%A9%EC%9D%98-%EC%A7%80%EB%A6%84/quiz/1

n, m = map(int, input().split())
ants = sorted(list(map(int, input().split())))
left, right = 0, 0
result = 0
while right < n:
	
	while right < n and ants[right] - ants[left] <= m:
		right += 1
	
	result = max(result, right-left)
	
	left += 1

print(n- result)

# 3 1
# 2 1 4

# 1

# 3 0
# 7 7 7

# 0

# 6 3
# 1 3 4 6 9 10

# 3

# 11 5
# 10 11 12 13 14 15 16 17 18 19 20

# 5
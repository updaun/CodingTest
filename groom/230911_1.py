# 구름LEVEL
# 인공지능 청소기
# https://level.goorm.io/exam/43068/1a-%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5-%EC%B2%AD%EC%86%8C%EA%B8%B0/quiz/1

t = int(input())
for i in range(t):
	x, y, n = map(int, input().split())
	r = abs(x)+abs(y)
	if r <= n and r%2 == n%2:
		print("YES")
	else:
		print("NO")

# 4
# -5 -2 7
# 5 -5 2
# 0 5 6
# 1 2 7

# YES
# NO
# NO
# YES
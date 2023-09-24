# 구름LEVEL
# 합 계산기
# https://level.goorm.io/exam/195685/%ED%95%A9-%EA%B3%84%EC%82%B0%EA%B8%B0/quiz/1

n = int(input())
result = 0
for i in range(n):
	a, c, b = input().split()
	a, b = int(a), int(b)
	if c == "+":
		result += a+b
	elif c == "-":
		result += a-b
	elif c == "*":
		result += a*b
	elif c == "/":
		result += a//b
print(result)
		
# 3
# 1 + 3
# 4 / 3
# 3 - 2

# 6

# 3
# 3 - 4
# 4 / 5
# 5 * 1

# 4
# 구름LEVEL
# 통증 (2)
# https://level.goorm.io/exam/195693/%ED%86%B5%EC%A6%9D-2/quiz/1

t = int(input())
a, b = map(int, input().split())
memo = []
m, n = divmod(t, b)
for i in range(t//b+1):
	temp, remain = divmod((n+(i*b)),a)
	if remain == 0:
		memo.append(m-i+temp)
		break
if len(memo) == 0:
	print(-1)
else:
	print(min(memo))
	
# 11
# 2 7

# 3

# 10000
# 4 13

# 772

# 10
# 3 5

# 2
# 구름LEVEL
# 어려운 문제
# https://level.goorm.io/exam/49054/%EC%96%B4%EB%A0%A4%EC%9A%B4-%EB%AC%B8%EC%A0%9C/quiz/1

import math
n = int(input())
target = list(str(math.factorial(n)))
while len(target) >= 2:
	temp = sum(list(map(int, target)))
	target = list(str(temp))
print(target[0])

# 10

# 9

# 4

# 6

# 5

# 3

# 4021

# 9
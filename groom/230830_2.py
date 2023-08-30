# 구름LEVEL
# 거스름 돈
# https://level.goorm.io/exam/175177/%EA%B1%B0%EC%8A%A4%EB%A6%84-%EB%8F%88/quiz/1

coins = [40, 20, 10, 5, 1]
returns = 0
c = int(input())
for coin in coins:
	a, c = divmod(c, coin)
	returns += a
print(returns)

# 55

# 3

# 39

# 7

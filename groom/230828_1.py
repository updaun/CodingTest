# 구름LEVEL
# 피보나치 수
# https://level.goorm.io/exam/175018/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98/quiz/1

# Memoization
n = int(input())

def n_list(n):
	memo = [0, 0, 1]
	for i in range(3, n+1):
		memo.append(memo[i-1] + memo[i-2])
	return memo[n]

print(n_list(n) % 1000000007)

# 6
# 5

# 10
# 34
# 구름LEVEL
# 보드 게임
# https://level.goorm.io/exam/177450/%EB%B3%B4%EB%93%9C-%EA%B2%8C%EC%9E%84/quiz/1

n = int(input())

def board_game(n):
	memo = [1, 1, 1, 2]
	for i in range(4, n+1):
		memo.append(memo[i-1]+memo[i-3])
	return memo[n]

print(board_game(n) % 1000000007)

# 6

# 6

# 7

# 9

# 49584

# 871579385
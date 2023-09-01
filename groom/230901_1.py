# 구름LEVEL
# 0 채우기
# https://level.goorm.io/exam/175011/0-%EC%B1%84%EC%9A%B0%EA%B8%B0/quiz/1

n = int(input())
result = 0
n_list = [list(map(int, input().split())) for i in range(n)]
for i, i_list in enumerate(n_list):
	if 0 in i_list:
		r, h = i, i_list.index(0)
for n in n_list:
	result += n[h]
print(result + sum(n_list[r]))

# 3
# 3 0 3
# 2 4 2
# 2 2 1

# 12

# 4
# 1 4 5 4
# 2 3 5 3
# 4 4 3 4
# 1 5 4 0

# 21

# 구름LEVEL
# 장마
# https://level.goorm.io/exam/194982/%EC%9E%A5%EB%A7%88/quiz/1

n, m = map(int, input().split())
k_list = list(map(int, input().split()))
check = []
for i in range(1, m+1):
	s, e = map(int, input().split())
	
	for j in range(s-1, e):
		k_list[j] += 1
		check.append(j)
	if i % 3 == 0:
		for a in set(check):
			k_list[a] -= 1
		check = []
print(" ".join(map(str, k_list)))

# 5 5
# -1 0 1 0 2
# 1 1
# 2 2
# 3 3
# 4 5
# 4 5

# -1 0 1 2 4

# 5 7
# 0 0 0 0 0
# 1 5
# 1 5
# 1 5
# 1 5
# 1 5
# 1 5
# 1 2

# 5 5 4 4 4
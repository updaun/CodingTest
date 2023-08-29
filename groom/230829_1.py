# 구름LEVEL
# 구름 스퀘어
# https://level.goorm.io/exam/175194/%EA%B5%AC%EB%A6%84-%EC%8A%A4%ED%80%98%EC%96%B4/quiz/1

# 그리디 알고리즘 최적해 구하기
n = int(input())
n_list = sorted([list(map(int, input().split())) for i in range(n)], key=lambda x:x[1])
result = [n_list[0]]
for i in range(1, n):
	s, e = n_list[i]
	if result[-1][1] < s:
		result.append(n_list[i])
print(len(result))	

# 6
# 1 2
# 2 3
# 3 6
# 4 5
# 1 10
# 11 13

# 3

# 7
# 1 2
# 3 3
# 3 5
# 4 10
# 5 6
# 7 9
# 10 11

# 5

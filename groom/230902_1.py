# 구름LEVEL
# 밀도 정렬
# https://level.goorm.io/exam/174784/%EB%B0%80%EB%8F%84-%EC%A0%95%EB%A0%AC/quiz/1

n = int(input())
result = []
for i in range(1, n+1):
	w, v = map(int, input().split())
	result.append([i, w, v, w/v])
print(sorted(result, key=lambda x:(-x[3],-x[1],x[0]))[0][0])

# 4
# 1 2
# 2 1
# 3 1
# 5 1

# 4

# 4
# 10 1
# 10 2
# 10 1
# 10 2

# 1

# 4
# 2 1
# 4 2
# 8 4
# 16 8

# 4
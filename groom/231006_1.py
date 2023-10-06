# 구름LEVEL
# 과일 구매
# https://level.goorm.io/exam/195697/%EA%B3%BC%EC%9D%BC-%EA%B5%AC%EB%A7%A4/quiz/1

n, k = map(int, input().split())
f = [list(map(int, input().split())) for _ in range(n)]

f.sort(key=lambda x:x[1]//x[0])

total = 0

while k and f:
	p, c = f.pop()
	if k>= p:
		total += c
		k -= p
	else:
		total += c//p*k
		k = 0
print(total)


# 6 13
# 2 8
# 7 35
# 1 5
# 3 12
# 10 30
# 1 7

# 63

# 5 4
# 1 999999996
# 1 999999997
# 1 999999998
# 1 999999999
# 1 1000000000

# 3999999994

# 1 1
# 1000000000 1000000000

# 1
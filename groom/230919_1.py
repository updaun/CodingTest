# 구름LEVEL
# 블록 게임
# https://level.goorm.io/exam/191052/%EB%B8%94%EB%A1%9D-%EA%B2%8C%EC%9E%84/quiz/1

m = int(input())
d = list(input().rstrip())
s = list(map(int, input().split()))

blocks = [(0,0)]
stack = [1]

for i, (j,k) in enumerate(zip(d, s)):
	x,y = blocks[-1]
	if j == "R":
		target = (x+1, y)
	elif j == "L":
		target = (x-1, y)
	elif j == "U":
		target = (x, y+1)
	elif j == "D":
		target = (x, y-1)
	
	if target in blocks:
		r = blocks.index(target)
		blocks = blocks[:r]
		stack = stack[:r]
	blocks.append(target)
	stack.append(k)
print(sum(stack))

# 5
# RRULD
# 5 2 4 3 2

# 3

# 6
# RRRUUU
# 8 4 6 5 2 2

# 28
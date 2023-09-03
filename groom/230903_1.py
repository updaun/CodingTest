# 구름LEVEL
# 단어 필터
# https://level.goorm.io/exam/174760/%EB%8B%A8%EC%96%B4-%ED%95%84%ED%84%B0/quiz/1

l_s, l_e = map(int, input().split())
s = input().rstrip()
e = input().rstrip()

stack = []

for i in e:
	stack.append(i)
	if len(stack) >= l_s and "".join(stack[-l_s:])==s:
		for _ in range(l_s):
			stack.pop()
if len(stack) == 0:
	print("EMPTY")
else:
	print("".join(stack))

# 5 10
# GOORM
# BwDcVGOORM

# BwDcV

# 5 12
# goorm
# goormabgoorm

# ab

# 1 5
# A
# AAAAA

# EMPTY
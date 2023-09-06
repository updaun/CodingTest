# 구름LEVEL
# Stack
# https://level.goorm.io/exam/175240/stack/quiz/1

n, k = map(int, input().split())
stack = []
for i in range(n):
	c = input().split()
	if c[0] == "push":
		if len(stack) < k:
			stack.append(c[1])
		else:
			print("Overflow")
	else:
		if len(stack) > 0:
			print(stack.pop())
		else:
			print("Underflow")
			

# 10 3
# push 1
# push 6
# push 5
# pop
# pop
# pop
# push 4
# push 4
# push 3
# pop

# 5
# 6
# 1
# 3

# 5 3
# pop
# push 4
# push 9
# push 9
# push 2

# Underflow
# Overflow

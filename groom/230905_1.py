# 구름LEVEL
# Queue
# https://level.goorm.io/exam/170831/%EA%B5%AC%EB%A6%84-%EC%95%84%EC%9D%B4%EB%8F%8C/quiz/1

from collections import deque

n, k = map(int, input().split())
q = deque(maxlen=k)
for i in range(n):
	c = input().split()
	if c[0] == "push":
		if len(q) < k:
			q.append(c[1])
		else:
			print("Overflow")
	else:
		if len(q)!=0:
			print(q.popleft())
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

# 1
# 6
# 5
# 4

# 5 3
# pop
# push 4
# push 9
# push 9
# push 2

# Underflow
# Overflow

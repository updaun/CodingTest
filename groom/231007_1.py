# 구름LEVEL
# 연합
# https://level.goorm.io/exam/195698/%EC%97%B0%ED%95%A9/quiz/1

from collections import deque
N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)
result = 0
for i in range(M):
	s, e = map(int, input().split())
	graph[s].append(e)

for i in range(1, N+1):
	if visited[i]:
		continue
	
	q = deque([i])
	result += 1
	visited[i] = 1
	
	while q:
		now = q.popleft()
		for to in graph[now]:
			if not visited[to] and now in graph[to]:
				q.append(to)
				visited[to] = 1
print(result)

# 4 6
# 2 3
# 4 1
# 1 2
# 3 4
# 1 4
# 2 4

# 3

# 3 6
# 1 2
# 1 3
# 2 1
# 2 3
# 3 1
# 3 2

# 1

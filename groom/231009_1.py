# 구름LEVEL
# 그래프의 밀집도
# https://level.goorm.io/exam/195699/%EA%B7%B8%EB%9E%98%ED%94%84%EC%9D%98-%EB%B0%80%EC%A7%91%EB%8F%84/quiz/1

from collections import deque

def bfs(start):
	q = deque([start])
	component = set()
	
	while q:
		now = q.popleft()
		
		if visited[now]:
			continue
		visited[now] = 1
		component.add(now)
		
		for to in graph[now]:
			if not visited[to]:
				q.append(to)
		
	edge = 0
		
	for i in component:
		for to in graph[i]:
			if to in component:
				edge += 1
					
	return sorted(list(component)), edge/len(component)

N, M = map(int, input().split())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
	s, e = map(int, input().split())
	graph[s].append(e)
	graph[e].append(s)
result, density = [], 0


for i in range(N+1):
	if not visited[i]:
		temp, tempDensity = bfs(i)
		
		if tempDensity > float(density):
			result = temp
			density = tempDensity
		elif tempDensity == float(density):
			if len(result) > len(temp):
				result = temp
				density = tempDensity
			elif len(result) == len(temp):
				if temp[0] < result[0]:
					result = temp
					density = tempDensity
print(*result)

# 7 6
# 1 3
# 5 3
# 3 7
# 7 1
# 2 4
# 4 6

# 1 3 5 7

# 6 6
# 2 3
# 5 3
# 2 6
# 1 2
# 1 4
# 5 4

# 1 2 3 4 5 6 

# 17 4
# 16 17
# 3 16
# 1 17
# 7 5

# 1 3 16 17 
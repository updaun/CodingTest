# 구름LEVEL
# 대체 경로
# https://level.goorm.io/exam/195701/%EB%8C%80%EC%B2%B4-%EA%B2%BD%EB%A1%9C/quiz/1

from collections import deque

def bfs(start, off):
	if start == off:
		return -1
	visited = [0]*(N+1)
	q = deque([start])
	visited[start]=1
	step = 1
	
	while q:
		step += 1
		for _ in range(len(q)):
			now = q.popleft()
			
			for to in graph[now]:
				if visited[to] or to == off:
					continue
				if to == E:
					return step
			
				visited[to] = 1
				q.append(to)
	return -1

N, M, S, E = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)
	
for i in range(1, N+1):
	print(bfs(S, i))
	

# 5 5 1 4
# 1 3
# 4 3
# 2 5
# 4 2
# 1 5

# -1
# 3
# 4
# -1
# 3

# 4 4 3 1
# 4 1
# 4 3
# 3 2
# 2 1

# -1
# 3
# -1
# 3

# 9 10 1 9
# 1 2
# 1 3
# 3 4
# 2 5
# 4 5
# 5 6
# 6 7
# 5 8
# 7 9
# 8 9

# -1
# 6
# 5
# 5
# -1
# 5
# 5
# 6
# -1
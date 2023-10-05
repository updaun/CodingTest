# 구름LEVEL
# 작은 노드
# https://level.goorm.io/exam/195696/%EC%9E%91%EC%9D%80-%EB%85%B8%EB%93%9C/quiz/1

from collections import deque

def bfs(start):
	q = deque([start])
	while q:
		now = q.popleft()
		visited[now] = 1
		for to in sorted(g[now]):
			if not visited[to]:
				q.append(to)
				break
		else:
			return now

n, m, k = map(int, input().split())
g = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(m):
	s, e = map(int, input().split())
	g[s].append(e)
	g[e].append(s)

result = bfs(k)
print(sum(visited), result)


# 6 6 1
# 1 2
# 1 3
# 2 3
# 3 4
# 3 5
# 4 6

# 5 6

# 6 5 1
# 1 2
# 2 3
# 3 4
# 4 5
# 5 6

# 6 6

# 6 5 1
# 2 3
# 3 2
# 6 2
# 4 2
# 4 3

# 1 1
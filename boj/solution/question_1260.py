import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
q = deque([], maxlen=(n+1))
d = [[] for i in range(n+1)]
visited = [False]*(n+1)
dfs_resule = []
bfs_resule = []

for i in range(m):
    s, e = map(int, input().split())
    d[s].append(e)
    d[e].append(s)
d = [sorted(i) for i in d] 

def dfs(curr):
    visited[curr] = True
    dfs_resule.append(curr)
    for next in d[curr]:
        if not visited[next]:
            dfs(next)

def bfs(curr):
    q.append(curr)
    visited[curr] = True
    while len(q) != 0:
        curr = q.popleft()
        bfs_resule.append(curr)
        for next in d[curr]:
            if not visited[next]:
                visited[next] = True
                q.append(next)

dfs(v)
print(' '.join(map(str, dfs_resule)))
visited = [False]*(n+1)
bfs(v)
print(' '.join(map(str, bfs_resule)))
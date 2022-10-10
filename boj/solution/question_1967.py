import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
d = [[] for _ in range(n+1)]

def dfs(x, w):
    for i in d[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = w + b
            dfs(a, w+b)

for _ in range(n-1):
    a, b, c = map(int, input().split())
    d[a].append([b, c])
    d[b].append([a, c])

distance = [-1]*(n+1)
distance[1] = 0
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)
print(max(distance))

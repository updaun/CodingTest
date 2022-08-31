import sys
input = sys.stdin.readline
com = int(input())
d = [[] for i in range(com+1)]
v = [False] * (com+1)
result = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

def dfs(curr):
    global result
    v[curr] = True
    result += 1
    for next in d[curr]:
        if not v[next]:
            dfs(next)
dfs(1)
print(result-1)
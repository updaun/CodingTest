import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = [sorted(list(map(int, input().split())), reverse=True) for i in range(n)]
score = [0]*(n)
for i in range(m):
    r = [d[j][i] for j in range(n)]
    for t in range(n):
        if r[t] == max(r):
            score[t] += 1
win = [i+1 for i in range(n) if score[i]==max(score)]
print(*win)

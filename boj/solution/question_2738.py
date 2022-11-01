import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(n)]
result = [[a[j][i]+b[j][i] for i in range(m)] for j in range(n)]
for row in result:
    print(*row)
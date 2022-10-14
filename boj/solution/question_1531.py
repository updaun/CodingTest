import sys
input = sys.stdin.readline
d = [[0]*100 for _ in range(100)]
n, m = map(int, input().split())
for _ in range(n):
    x, y, nx, ny = [i-1 for i in list(map(int, input().split()))]
    for i in range(x, nx+1):
        for j in range(y, ny+1):
            d[i][j] += 1
result = 0
for row in d:
    result += len([p for p in row if p > m])
print(result)

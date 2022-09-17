import sys
input = sys.stdin.readline
d = [[False]*100 for _ in range(100)]
result = 0
for i in range(int(input())):
    x, y = map(int, input().split())
    for a in range(y, y+10):
        for b in range(x, x+10):
            d[a][b] = True
for i in range(100):
    for j in range(100):
        if d[j][i]:
            result +=1
print(result)

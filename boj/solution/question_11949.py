import sys
input = sys.stdin.readline
n, m = map(int, input().split())
c = []
for i in range(n):
    c.append(int(input()))
for i in range(1, m+1):
    for j in range(n-1):
        if c[j]%i > c[j+1]%i:
            temp = c.pop(j)
            c.insert(j+1, temp)
print("\n".join(map(str, c)))
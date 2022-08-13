import sys
input = sys.stdin.readline
n, t = map(int, input().split())
works = list(map(int, input().split()))
result = 0
for i in range(n):
    t -= works[i]
    if t < 0:
        break
    result += 1
print(result)

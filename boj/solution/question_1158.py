import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
d = deque(range(1, n+1))
while len(d) != 0:
    for i in range(k-1):
        d.rotate(-1)
    arr.append(d.popleft())
print(f"<{', '.join(map(str, arr))}>")
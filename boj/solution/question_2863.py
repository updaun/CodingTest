import sys
from collections import deque
input = sys.stdin.readline
a, b = map(int, input().split())
c, d = map(int, input().split())
q = deque([a, b, d, c])
result = []
for i in range(4):
    result.append(q[0]/q[3] + q[1]/q[2])
    q.rotate()
print(result.index(max(result)))
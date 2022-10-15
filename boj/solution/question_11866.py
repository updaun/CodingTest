from collections import deque
n, k = map(int, input().split())
d = deque(range(1, n+1))
temp = []
while d:
    for i in range(k-1):
        d.rotate(-1)
    temp.append(d.popleft())
print(f"<{', '.join(map(str, temp))}>")

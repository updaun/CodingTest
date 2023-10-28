from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
answer = []
while q:
    idx, paper = q.popleft()
    answer.append(idx+1)
    if paper > 0:
        q.rotate(-(paper-1))
    elif paper < 0:
        q.rotate(-paper)
print(*answer)
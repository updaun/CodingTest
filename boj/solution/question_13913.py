import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
s = [0]*100001
v = [0]*100001

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(s[x])

            arr = []
            temp = x
            for _ in range(s[x]+1):
                arr.append(temp)
                temp = v[temp]
            print(' '.join(map(str, arr[::-1])))

            return x

        for i in (x+1, x-1, 2*x):
            if 0 <= i <= 100000 and s[i]==0:
                q.append(i)
                s[i] = s[x]+1
                v[i] = x
    

bfs()
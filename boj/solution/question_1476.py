import sys
input = sys.stdin.readline
target = list(map(int, input().split()))
d = [0, 0, 0]
day = 0
while d != target:
    d = [i+1 for i in d]
    if d[0] > 15:
        d[0] = 1
    if d[1] > 28:
        d[1] = 1
    if d[2] > 19:
        d[2] = 1
    day += 1
print(day)
import sys
input = sys.stdin.readline
n = int(input())
t = list(map(int, input().split()))
m = int(input())
start, end = 0, max(t)
while start <= end:
    mid = (start+end)//2
    d = [i if i < mid else mid for i in t]
    if sum(d) > m:
        end = mid - 1
    else:
        start = mid + 1
print(end)
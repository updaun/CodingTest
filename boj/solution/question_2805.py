import sys
input = sys.stdin.readline
n, m = map(int, input().split())
t = list(map(int, input().split()))
start = 0
end = max(t)
while start <= end:
    mid = (start + end) // 2
    target = [tree-mid if tree-mid >= 0 else 0 for tree in t]
    if sum(target) >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
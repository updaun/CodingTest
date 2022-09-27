import sys
input = sys.stdin.readline
n = int(input())
pick = list(map(int, input().split()))
arr = []
for i in range(n):
    arr.insert(len(arr)-pick[i], i+1)
print(*arr)
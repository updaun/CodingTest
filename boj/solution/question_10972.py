import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
temp = -1

for i in range(n-1, 0, -1):
    if arr[i-1] < arr[i]:
        temp = i-1
        break
else:
    print(-1)
    sys.exit()

for i in range(n-1, 0, -1):
    if arr[temp] < arr[i]:
        arr[temp], arr[i] = arr[i], arr[temp]
        arr = arr[:temp+1]+sorted(arr[temp+1:])
        print(*arr)
        break
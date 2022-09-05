import sys
input = sys.stdin.readline
n, s = map(int, input().split())
d = list(map(int, input().split()))

count = 0

def back_tracking(idx, res):
    global count

    if idx >= n:
        return

    res += d[idx]

    if res == s:
        count += 1
            
    back_tracking(idx+1, res)
    back_tracking(idx+1, res-d[idx])

back_tracking(0, 0)
print(count)
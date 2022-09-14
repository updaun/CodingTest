import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
arr = []
w = 500
c = 0

def backtracking():
    global c
    global w
    if len(arr) == n:
        for i in arr:
            w += a[i]
            w -= k
            if w < 500:
                w = 500
                return
        c += 1
        w = 500
        return

    for i in range(n):
        if i not in arr:
            arr.append(i)
            backtracking()
            arr.pop()

backtracking()
print(c)
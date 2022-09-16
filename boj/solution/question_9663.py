# 30968ms
import sys
def n_queens(i, col):
    global count
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            count += 1
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)
def promising(i, col):
    k = 1
    flag = True
    while k < i and flag:
        if (col[k] == col[i]) or abs(col[k]-col[i]) == (i-k):
            flag = False
            return flag
        k += 1
    return flag

n = int(sys.stdin.readline())
col = [0] * (n+1)
count = 0
n_queens(0, col)
print(count)

# 시간 초과
# n = int(input())
# count = 0
# arr = []
# def backtracking():
#     global count
#     if len(arr) == n:
#         for i in range(n):
#             for j in range(1, n-i):
#                 if abs(arr[i]-arr[i+j])==j:
#                     return
#         count += 1
#         return
    
#     for i in range(n):
#         if i not in arr:
#             arr.append(i)
#             backtracking()
#             arr.pop()

# backtracking()
# print(count)

# 5100ms
n = int(input())
count = 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def backtracking(i):
    global count
    if i == n:
        count += 1
        return
    
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i+j] = c[i-j+n-1] = True
            backtracking(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False

backtracking(0)
print(count)

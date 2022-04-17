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
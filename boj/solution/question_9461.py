import sys
n = int(sys.stdin.readline())
t_list = [0, 1, 1, 1, 2] + [0] * 101
def dp(n):
    if t_list[n] != 0:
        return t_list[n]
    if n < 0:
        return 0
    else:
        temp = dp(n-1) + dp(n-5)
        t_list[n] = temp
        return temp
    
for i in range(n):
    target = int(sys.stdin.readline())
    print(dp(target))


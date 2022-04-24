import sys
def cal_gcd(n, m):
    if m == 0:
        return n
    else:
        return cal_gcd(m, n%m)

def cal_lcm(n, m):
    result = (n*m) // cal_gcd(n, m)
    return result

r = int(sys.stdin.readline())
n_list = []
for i in range(r):
    n, m = list(map(int, sys.stdin.readline().split()))
    n_list.append([n,m])

for i in n_list:
    n, m = i
    print(int(cal_lcm(n,m)))

'''
# 시간 초과 발생
import sys

r = int(sys.stdin.readline())
n_list = []
for i in range(r):
    n, m = list(map(int, sys.stdin.readline().split()))
    n_list.append([n,m])

for i in n_list:
    n, m = i
    div = 2
    result = 1
    while True:
        if min(n,m) < div:
            break
        if n%div == 0 and m%div == 0:
            n /= div
            m /= div 
            result *= div
        else:
            div += 1

    print(int(result *n*m))
'''
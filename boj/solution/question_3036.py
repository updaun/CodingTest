import sys

def cal_gcd(n, m):
    if m == 0:
        return n
    else:
        return cal_gcd(m, n%m)

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    gcd = cal_gcd(n_list[0], n_list[i])
    print(str(int(n_list[0]/gcd)) + "/" + str(int(n_list[i]/gcd)))
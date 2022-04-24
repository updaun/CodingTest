import sys
n, k = list(map(int, sys.stdin.readline().split()))

# 이항계수 binomial coefficient
# n!/(k!(n-k)!)
def bino_coef(n, k):
    if k == 0 or n == k:
        return 1
    return bino_coef(n-1, k) + bino_coef(n-1, k-1)

print(bino_coef(n,k))
import sys
input = sys.stdin.readline

def cal_gcd(n, m):
    if m == 0:
        return n
    else:
        return cal_gcd(m, n%m)

a, b = map(int, input().split())
c, d = map(int, input().split())

j = a*d+b*c
m = b*d

gcd = cal_gcd(j, m)
print(int(j/gcd), int(m/gcd))
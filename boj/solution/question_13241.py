# 백준
# 최소공배수
# https://www.acmicpc.net/problem/13241

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(a*b//gcd(a, b))
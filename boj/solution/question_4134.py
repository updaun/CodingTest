# 백준
# 다음 소수
# https://www.acmicpc.net/problem/4134

import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

n = int(input())
for i in range(n):
    t = int(input())
    while True:
        if is_prime(t):
            print(t)
            break
        t += 1

# 백준
# 17103번: 골드바흐 파티션
# https://www.acmicpc.net/problem/17103

import sys
input = sys.stdin.readline

prime = []
check = [0] * 1000001
check[0] = 1
check[1] = 1

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        for j in range(2*i, 1000001, i):
            check[j] = 1

for _ in range(int(input())):
    n = int(input())
    result = 0
    for i in prime:
        if i >= n:
            break
        if not check[n - i] and i <= n-i:
            result += 1
    print(result)
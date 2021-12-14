# boj 15552번 빠른 A+B
import sys

n = int(input())

for i in range(n):
    # a,b = map(int, input().split())
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(a+b)
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    num = input().rstrip()
    print(len(set([num[i]for i in range(len(num))])))
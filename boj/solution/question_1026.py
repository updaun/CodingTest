import sys
input = sys.stdin.readline
n = int(input())
A = sorted(list(map(int, input().split())), reverse=True)
B = sorted(list(map(int, input().split())))
print(sum([A[i]*B[i] for i in range(n)]))
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
f_dict = dict()
for i in range(N):
    f_dict[i+1] = 0
for i in range(M):
    A, B = map(int, input().split())
    f_dict[A] += 1
    f_dict[B] += 1
for i in range(N):
    print(f_dict[i+1])
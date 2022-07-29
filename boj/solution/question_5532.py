import sys
import math
input = sys.stdin.readline
vacation = []
for i in range(5):
    vacation.append(int(input()))
L, A, B, C, D = vacation
print(L - max(math.ceil(A/C), math.ceil(B/D)))
import sys
input = sys.stdin.readline
for i in range(int(input())):
    A = input().rstrip()
    B = input().rstrip()
    result = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            result += 1
    print(f'Hamming distance is {result}.')
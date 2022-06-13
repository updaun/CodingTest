import sys
A = int(sys.stdin.readline())
c = sys.stdin.readline().strip()
B = int(sys.stdin.readline())
if c == '*':
    print(A*B)
else:
    print(A+B)
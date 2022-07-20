import sys
input = sys.stdin.readline
n = int(input())
if n % 2 == 0:
    A = input().rstrip()
    B = input().rstrip()
    if A == B:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
else:
    A = input().rstrip()
    B = input().rstrip()
    new_A = ''
    for s in A:
        new_A += str(int(not bool(int(s))))
    if new_A == B:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
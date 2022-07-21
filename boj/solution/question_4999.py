import sys
input = sys.stdin.readline
me = input().rstrip()
doctor = input().rstrip()
if len(me) >= len(doctor):
    print('go')
else:
    print('no')
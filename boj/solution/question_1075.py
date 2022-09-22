import sys
input = sys.stdin.readline
n = int(input())
f = int(input())
for i in range(100):
    target = str(n)[:-2] + str(i).zfill(2)
    if int(target) % f == 0:
        print(str(i).zfill(2))
        break
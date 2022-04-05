import sys
n = int(sys.stdin.readline())

n_list=[0]*10001

for i in range(n):
    n_list[int(sys.stdin.readline())] += 1

for i in range(len(n_list)):
    if n_list[i] != 0:
        for j in range(n_list[i]):
            sys.stdout.write(str(i)+'\n')
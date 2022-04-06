import sys
n = sys.stdin.readline().strip()
n_list = []
for i in str(n):
    n_list.append(int(i))
n_list.sort()
for i in n_list[::-1]:
    sys.stdout.write(str(i))
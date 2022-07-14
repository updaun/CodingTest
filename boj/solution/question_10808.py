import sys
s = sys.stdin.readline().rstrip()
alpha_dict = {}
for k in 'abcdefghijklmnopqrstuvwxyz':
    alpha_dict[k] = 0
for i in s:
    alpha_dict[i] += 1
print(" ".join(map(str, alpha_dict.values())))

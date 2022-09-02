import sys
input = sys.stdin.readline
s_list = []
for i in range(int(input())):
    s_list.append(input().rstrip())
s_list = sorted(s_list, key=lambda x:(len(x), sum([int(i) if i.isdigit() else 0 for i in x]), x))
print("\n".join(map(str, s_list)))
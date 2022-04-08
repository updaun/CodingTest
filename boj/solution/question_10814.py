import sys
n = int(sys.stdin.readline())
profile_list = []
for i in range(n):
    profile = sys.stdin.readline().split()
    profile_list.append([int(profile[0]), profile[1]])
result = sorted(profile_list, key=lambda x:x[0])
for a,b in result:
    print(a, b)
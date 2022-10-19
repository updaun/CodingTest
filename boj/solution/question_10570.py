import sys
input = sys.stdin.readline
for _ in range(int(input())):
    num_dict = dict()
    for _ in range(int(input())):
        n = int(input())
        if n in num_dict.keys():
            num_dict[n] += 1
        else:
            num_dict[n] = 1
    print(sorted(num_dict, key=lambda x:(-num_dict[x], x))[0])

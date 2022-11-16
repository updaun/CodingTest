import sys
input = sys.stdin.readline
for i in range(int(input())):
    a, b = input().split()
    a_dict = dict()
    b_dict = dict()
    for s in a:
        if s in a_dict.keys():
            a_dict[s] += 1
        else:
            a_dict[s] = 1
    for s in b:
        if s in b_dict.keys():
            b_dict[s] += 1
        else:
            b_dict[s] = 1
    if a_dict == b_dict:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
        
import sys
N = int(sys.stdin.readline())
card_dict = dict()
for i in list(map(int, sys.stdin.readline().split())):
    if i not in card_dict.keys():
        card_dict[i] = 1
    else:
        card_dict[i] += 1
M = int(sys.stdin.readline())
question = list(map(int, sys.stdin.readline().split()))
print(" ".join(map(str, [card_dict[i] if i in card_dict.keys() else 0 for i in question])))
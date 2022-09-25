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

# 220924 신규 풀이 조금 더 느려짐
import sys
input = sys.stdin.readline
n = int(input())
n_dict = {}
for i in list(map(int, input().split())):
    if i in n_dict.keys():
        n_dict[i] += 1
    else:
        n_dict[i] = 1
m = int(input())
result = []
for i in list(map(int, input().split())):
    if i in n_dict.keys():
        result.append(n_dict[i])
    else:
        result.append(0)
print(*result)
import sys
input = sys.stdin.readline
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(input())):
    result = 0
    alpha_list = [i for i in alphabet]
    input_alpha = input().rstrip()
    input_alpha = [i for i in input_alpha]
    input_alpha = list(set(input_alpha))
    for s in input_alpha:
        alpha_list.remove(s)
    for v in alpha_list:
        result += ord(v)
    print(result)
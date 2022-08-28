import sys
input = sys.stdin.readline
while True:
    input_str = input().rstrip()
    if input_str == '#':
        break
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s_dict = {}
    for a in alphabet:
        s_dict[a] = 0
    for s in input_str:
        if s.isalpha():
            s_dict[s.lower()] += 1
    print(len([i for i in s_dict.keys() if s_dict[i] != 0]))

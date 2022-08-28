import sys
input = sys.stdin.readline
for i in range(int(input())):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    a_dict = {}
    for a in alphabet:
        a_dict[a] = 0
    name = input().rstrip()
    for s in name.lower():
        if s.isalpha(): 
            a_dict[s] += 1
    if a_dict['g'] > a_dict['b']:
        print(f'{name} is GOOD')
    elif a_dict['g'] < a_dict['b']:
        print(f'{name} is A BADDY')
    else:
        print(f'{name} is NEUTRAL')
        
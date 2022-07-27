import sys
input = sys.stdin.readline
alphabet = 'abcdefghijklmnopqrstuvwxyz'
while True:
    alphabet_list = [i for i in alphabet]
    sentence = input().rstrip()
    if sentence == '*':
        break
    for s in sentence:
        if s in alphabet_list:
            alphabet_list.remove(s)
    if len(alphabet_list) == 0:
        print('Y')
    else:
        print('N')
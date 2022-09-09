import sys
input = sys.stdin.readline
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(input())):
    input_s = input().rstrip()

    crypto = input().rstrip()
    crypto_dict = {}
    for i, s in enumerate(crypto):
        crypto_dict[alphabet[i]] = s
    result = ''
    for s in input_s:
        if s.isalpha():
            result += crypto_dict[s]
        else:
            result += s
    print(result)
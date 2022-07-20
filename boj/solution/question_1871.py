import sys
input = sys.stdin.readline
n = int(input())
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(n):
    LLL, DDDD = map(str, input().split('-'))
    result = 0
    for idx, s in enumerate(LLL):
        result += alphabet.index(s) * (26**(2-idx))
    if abs(result - int(DDDD)) <= 100:
        print('nice')
    else:
        print('not nice')

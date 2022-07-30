import sys
input = sys.stdin.readline
while True:
    bit_string = input().rstrip()
    result = bit_string[:-1]
    if bit_string == '#':
        break
    if bit_string[-1] == 'e':
        if bit_string.count('1') % 2 == 0:
            result += '0'
        else:
            result += '1'
    else:
        if bit_string.count('1') % 2 == 0:
            result += '1'
        else:
            result += '0'
    print(result)

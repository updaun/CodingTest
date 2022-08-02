import sys
input = sys.stdin.readline

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_dict = {}
temp = 1
for s in alphabet:
    alpha_dict[s] = temp
    temp += 1
while True:
    result = 0
    input_str = input().rstrip()
    if input_str == '#':
        break
    for i in range(len(input_str)):
        if input_str[i] != ' ':
            result += (i+1)*alpha_dict[input_str[i]]
    print(result)

import sys
input_string = sys.stdin.readline().rstrip()
reject_word = 'CAMBRIDGE'
reject_list = [i for i in reject_word]
result = ''
for s in input_string:
    if s not in reject_list:
        result += s
print(result)

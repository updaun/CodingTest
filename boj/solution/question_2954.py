import sys
sentence = sys.stdin.readline().rstrip()
result = ''
idx = 0
while idx != len(sentence):
    result += sentence[idx]
    if sentence[idx] in ['a', 'e', 'i', 'o', 'u']:
        idx += 3
    else:
        idx += 1
print(result)
        
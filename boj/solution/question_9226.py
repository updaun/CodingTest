import sys
input = sys.stdin.readline

while True:
    word = input().rstrip()
    if word == '#':
        break
    result = ''
    target = -1
    for i in range(len(word)):
        if word[i] in ['a', 'e', 'i', 'o', 'u']:
            target = i
            break
    if target == -1:
        result = word + "ay"
    else:
        result = word[target:] + word[:target] + "ay"
    print(result)
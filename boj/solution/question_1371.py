alphabet = dict()
max_alpha = []
while True:
    try:
        for s in input().rstrip():
            if s != ' ':
                if s not in alphabet.keys():
                    alphabet[s] = 1
                else:
                    alphabet[s] += 1
    except EOFError:
        break
for s in alphabet:
    if alphabet[s] == max(alphabet.values()):
        max_alpha.append(s)
print(''.join(map(str, sorted(max_alpha))))
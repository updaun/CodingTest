result = ''
while True:
    try:
        result += input()
    except EOFError:
        break
print(sum(list(map(int, result.split(',')))))
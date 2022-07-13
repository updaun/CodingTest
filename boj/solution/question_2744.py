import sys
result = ''
for s in sys.stdin.readline().rstrip():
    if s.islower():
        result += s.upper()
    else:
        result += s.lower()
print(result)

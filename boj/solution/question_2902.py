import sys
result = ''
for i in sys.stdin.readline().split('-'):
    result += i[0]
print(result)
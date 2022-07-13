import sys
count = 0
for s in sys.stdin.readline().rstrip():
    count += int(s in ['a', 'e', 'i', 'o', 'u'])
print(count)
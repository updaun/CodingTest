import sys
input = sys.stdin.readline

temp = 0

for _ in range(int(input())):
    line = input().split()
    if len(line) == 2:
        command, n = line
        n = int(n)-1
        if command == 'add':
            temp = temp | (1 << n)
        elif command == 'remove':
            temp = temp & ~(1 << n)
        elif command == 'check':
            if temp & (1 << n) == 0:
                print(0)
            else:
                print(1)
        elif command == 'toggle':
            temp = temp ^ (1 << n)
    else:
        if line[0] == 'all':
            temp = temp | ((1 << 20) - 1)
        else:
            temp = 0
            
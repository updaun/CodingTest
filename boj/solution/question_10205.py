import sys
input = sys.stdin.readline
for t in range(int(input())):
    h = int(input())
    c = input().rstrip()
    for a in c:
        if a == 'c':
            h += 1
        else:
            h -= 1
    print(f"Data Set {t+1}:\n{h}\n")
import sys
input = sys.stdin.readline
for i in range(int(input())):
    a,b,c =sorted(list(map(int, input().split())))
    print(f"Scenario #{i+1}:")
    if a**2+b**2 == c**2:
        print('yes\n')
    else:
        print('no\n')
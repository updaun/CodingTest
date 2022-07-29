import sys
input = sys.stdin.readline
for i in range(int(input())):
    flower = input().rstrip()
    target = int(len(flower) / 2) 
    if flower[target-1] == flower[target]:
        print('Do-it')
    else:
        print('Do-it-Not')
import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    scores = sorted(list(map(int, input().split())))
    if scores[3]-scores[1] >= 4:
        print("KIN")
    else:
        print(sum(scores[1:-1]))
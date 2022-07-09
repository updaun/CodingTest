import sys
input = sys.stdin.readline
k = int(input())
for i in range(k):
    p, m = map(int, input().split())
    seet = [i for i in range(1,m+1)]
    count = 0
    for j in range(p):
        player = int(input())
        if player in seet:
            seet.remove(player)
        else:
            count += 1
    print(count)
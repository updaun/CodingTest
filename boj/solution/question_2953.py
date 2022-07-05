import sys
players = []
for i in range(1, 6):
    players.append([i, sum(list(map(int, sys.stdin.readline().split())))])
print(" ".join(map(str, sorted(players, key=lambda x:x[1])[-1])).rstrip())
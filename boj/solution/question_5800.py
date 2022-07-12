import sys
input = sys.stdin.readline
for i in range(1, int(input())+1):
    print(f"Class {i}")
    scores = sorted(list(map(int, input().split()))[1:])
    gap = [scores[i]-scores[i-1] for i in range(1, len(scores))]
    print(f"Max {scores[-1]}, Min {scores[0]}, Largest gap {max(gap)}")
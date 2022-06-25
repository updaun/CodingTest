import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    score = 0
    mean = 0
    for _ in range(N):
        C, G = map(float, sys.stdin.readline().split())
        score += C
        mean += G*C
    print(int(score), round(mean/score, 1))

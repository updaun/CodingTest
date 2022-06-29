import sys
score_str = "EABCD"
for i in range(3):
    play = list(map(int, sys.stdin.readline().split()))
    b_count = play.count(0)
    print(score_str[b_count])

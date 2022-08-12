import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ball_list = [0 for i in range(n)]
for i in range(m):
    s, f, num = map(int, input().split())
    for t in range(s-1, f):
        ball_list[t] = num
print(" ".join(map(str, ball_list)))
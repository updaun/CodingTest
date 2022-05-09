import sys

n = int(sys.stdin.readline())
rgb_list = []

for i in range(n):
    rgb_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    rgb_list[i][0] = rgb_list[i][0] + min(rgb_list[i-1][1], rgb_list[i-1][2])
    rgb_list[i][1] = rgb_list[i][1] + min(rgb_list[i-1][0], rgb_list[i-1][2])
    rgb_list[i][2] = rgb_list[i][2] + min(rgb_list[i-1][0], rgb_list[i-1][1])

print(min(rgb_list[n-1]))
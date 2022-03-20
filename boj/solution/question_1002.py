import math
n = int(input())
target_list = []

for i in range(n):
    target_list.append(tuple(map(int, input().split(" "))))

for t in target_list:
    x1, y1, r1, x2, y2, r2 = t
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    target = 0
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            target = -1
    else:
        if distance == r1+r2 or distance == abs(r1-r2):
            target = 1
        elif distance < r1+r2 and distance > abs(r1-r2):
            target = 2
    print(target)
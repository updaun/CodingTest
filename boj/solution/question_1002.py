import math
n = int(input())
target_list = []

for i in range(n):
    target_list.append(tuple(map(int, input().split(" "))))

for t in target_list:
    x1, y1, r1, x2, y2, r2 = t
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    threshold = distance - r1 - r2
    target = 0
    if x1 == x2 and y1 == y2 and r1 == r2:
        target = -1
    # elif distance <= r1 or distance <= r2:
    #     target = 0
    elif threshold < 0:
        target = 2
    elif threshold == 0 or (r1 - distance == r2) or (r2 - distance == r1):
        target = 1
    print(target)

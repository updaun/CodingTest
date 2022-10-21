import sys
d, k = map(int, input().split())
x1, y1 = 1, 0
x2, y2 = 1, 1
temp1, temp2 = 0, 0
for i in range(1, d+1):
    if i == 1:
        x, y = x1, y1
    elif i == 2:
        x, y = x2, y2
    else:
        x = x1+x2
        y = y1+y2
        x1, y1 = x2, y2
        x2, y2 = x, y
for i in range(1, k+1):
    for j in range(1, k+1):
        if i <= j:
            if x*i+y*j == k:
                print(i)
                print(i+j)
                sys.exit(0)
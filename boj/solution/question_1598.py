m,n = map(int, input().split())
x1,y1 = divmod(m, 4)
x2,y2 = divmod(n, 4)
if y1 == 0:
    x1 -= 1
    y1 = 4
if y2 == 0:
    x2 -= 1
    y2 = 4
print(abs(x1-x2)+abs(y1-y2))
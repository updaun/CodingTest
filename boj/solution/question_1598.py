m,n = map(int, input().split())
x1,y1 = divmod(m, 4)
x2,y2 = divmod(n, 4)
print(abs(x1-x2)+abs(y1-y2))
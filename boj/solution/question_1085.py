x,y,w,h = tuple(map(int, input().split(" ")))
print(sorted([x,y,w-x,h-y])[0])
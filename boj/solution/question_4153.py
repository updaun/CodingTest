t = list(map(int, input().split(" ")))

while t != [0,0,0]:
    t.sort()
    if t[0]**2 + t[1]**2 == t[2]**2:
        print("right")
    else:
        print("wrong")
    t = list(map(int, input().split(" ")))